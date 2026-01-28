from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, send_from_directory, make_response, Blueprint
import sqlite3
import os
from werkzeug.utils import secure_filename
from flask_restx import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'd8f9#KJf9@2!sL0pQw8xZ@2026' 

# --- CONFIGURATION ---
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static/uploads')
app.config['DATABASE'] = os.path.join(BASE_DIR, 'database.db')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"

# --- DATABASE HELPERS ---
def get_db_connection():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            image TEXT,
            date_posted TEXT NOT NULL,
            likes INTEGER DEFAULT 0,
            shares INTEGER DEFAULT 0
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            date_posted TEXT NOT NULL,
            likes INTEGER DEFAULT 0,
            FOREIGN KEY (post_id) REFERENCES posts (id)
        )
    ''')
    try:
        conn.execute('SELECT likes FROM comments LIMIT 1')
    except sqlite3.OperationalError:
        conn.execute('ALTER TABLE comments ADD COLUMN likes INTEGER DEFAULT 0')
    conn.commit()
    conn.close()

with app.app_context():
    init_db()

# --- 1. SETUP API & SWAGGER (WITH BLUEPRINT) ---
# This separates API from the Website to avoid conflicts.
# Docs are at: http://YOUR-SITE/api/docs
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/docs', title="Full Blog API", description="Complete API for Testing: Auth, Posts, Comments, Likes")
app.register_blueprint(blueprint)

# --- API PARSERS (For Swagger Inputs) ---
# Parser for Login
login_parser = reqparse.RequestParser()
login_parser.add_argument('username', required=True, help="Admin Username")
login_parser.add_argument('password', required=True, help="Admin Password")

# Parser for Creating/Editing Posts (Handles Image Uploads)
post_parser = reqparse.RequestParser()
post_parser.add_argument('title', required=True, help="Post Title")
post_parser.add_argument('content', required=True, help="Post Content")
post_parser.add_argument('image', location='files', type=FileStorage, required=False, help="Post Image")

# Parser for Comments
comment_parser = reqparse.RequestParser()
comment_parser.add_argument('content', required=True, help="Comment text")

# --- API RESOURCES (ALL FUNCTIONALITIES) ---

@api.route('/login')
class LoginResource(Resource):
    @api.expect(login_parser)
    @api.doc(description="Log in to perform Admin actions (Create/Edit/Delete)")
    def post(self):
        args = login_parser.parse_args()
        if args['username'] == ADMIN_USERNAME and args['password'] == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return {'status': 'success', 'message': 'Logged in successfully'}, 200
        return {'status': 'error', 'message': 'Invalid credentials'}, 401

@api.route('/posts')
class PostListResource(Resource):
    @api.doc(description="Get all posts")
    def get(self):
        conn = get_db_connection()
        posts = conn.execute('SELECT * FROM posts ORDER BY date_posted DESC').fetchall()
        conn.close()
        return {'posts': [dict(p) for p in posts]}, 200

    @api.expect(post_parser)
    @api.doc(description="Create a new post (Requires Login)")
    def post(self):
        if not session.get('admin_logged_in'):
            return {'status': 'error', 'message': 'Unauthorized'}, 401
        
        args = post_parser.parse_args()
        image = args['image']
        filename = None
        
        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        date_posted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = get_db_connection()
        cur = conn.execute('INSERT INTO posts (title, content, image, date_posted) VALUES (?, ?, ?, ?)',
                     (args['title'], args['content'], filename, date_posted))
        conn.commit()
        new_id = cur.lastrowid
        conn.close()
        return {'status': 'success', 'id': new_id, 'message': 'Post created'}, 201

@api.route('/posts/<int:id>')
@api.doc(params={'id': 'Post ID'})
class PostResource(Resource):
    @api.doc(description="Get a single post details")
    def get(self, id):
        conn = get_db_connection()
        post = conn.execute('SELECT * FROM posts WHERE id = ?', (id,)).fetchone()
        conn.close()
        if post:
            return dict(post), 200
        return {'error': 'Post not found'}, 404

    @api.expect(post_parser)
    @api.doc(description="Edit a post (Requires Login)")
    def put(self, id):
        if not session.get('admin_logged_in'):
            return {'status': 'error', 'message': 'Unauthorized'}, 401
            
        args = post_parser.parse_args()
        conn = get_db_connection()
        
        if args['image']:
            filename = secure_filename(args['image'].filename)
            args['image'].save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            conn.execute('UPDATE posts SET title = ?, content = ?, image = ? WHERE id = ?',
                         (args['title'], args['content'], filename, id))
        else:
            conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?',
                         (args['title'], args['content'], id))
        conn.commit()
        conn.close()
        return {'status': 'success', 'message': 'Post updated'}, 200

    @api.doc(description="Delete a post (Requires Login)")
    def delete(self, id):
        if not session.get('admin_logged_in'):
            return {'status': 'error', 'message': 'Unauthorized'}, 401
            
        conn = get_db_connection()
        conn.execute('DELETE FROM posts WHERE id = ?', (id,))
        conn.execute('DELETE FROM comments WHERE post_id = ?', (id,))
        conn.commit()
        conn.close()
        return {'status': 'success', 'message': 'Post deleted'}, 200

@api.route('/posts/<int:id>/comment')
@api.doc(params={'id': 'Post ID to comment on'})
class CommentResource(Resource):
    @api.expect(comment_parser)
    @api.doc(description="Add a comment to a post")
    def post(self, id):
        args = comment_parser.parse_args()
        date_posted = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        conn = get_db_connection()
        conn.execute('INSERT INTO comments (post_id, content, date_posted, likes) VALUES (?, ?, ?, 0)', 
                     (id, args['content'], date_posted))
        conn.commit()
        conn.close()
        return {'status': 'success', 'message': 'Comment added'}, 201

@api.route('/like/<int:id>')
@api.doc(params={'id': 'Post ID'})
class LikePostResource(Resource):
    @api.doc(description="Like a post")
    def post(self, id):
        liked_cookie = request.cookies.get(f'liked_post_{id}')
        conn = get_db_connection()
        if not liked_cookie:
            conn.execute('UPDATE posts SET likes = likes + 1 WHERE id = ?', (id,))
            conn.commit()
        post = conn.execute('SELECT likes FROM posts WHERE id = ?', (id,)).fetchone()
        conn.close()
        
        response = make_response(jsonify({'likes': post['likes'], 'status': 'success' if not liked_cookie else 'already_liked'}))
        if not liked_cookie:
            response.set_cookie(f'liked_post_{id}', 'true', max_age=31536000)
        return response

@api.route('/like_comment/<int:id>')
@api.doc(params={'id': 'Comment ID'})
class LikeCommentResource(Resource):
    @api.doc(description="Like a comment")
    def post(self, id):
        liked_cookie = request.cookies.get(f'liked_comment_{id}')
        conn = get_db_connection()
        if not liked_cookie:
            conn.execute('UPDATE comments SET likes = likes + 1 WHERE id = ?', (id,))
            conn.commit()
        comment = conn.execute('SELECT likes FROM comments WHERE id = ?', (id,)).fetchone()
        conn.close()
        
        response = make_response(jsonify({'likes': comment['likes']}))
        if not liked_cookie:
            response.set_cookie(f'liked_comment_{id}', 'true', max_age=31536000)
        return response

# --- WEB ROUTES (HTML - Keeping these for the Website Users) ---

@app.route('/robots.txt')
def robots(): return send_from_directory(BASE_DIR, 'robots.txt')

@app.route('/sitemap.xml')
def sitemap(): return send_from_directory(BASE_DIR, 'sitemap.xml')

@app.route('/')
def index(): return render_template('index.html')

@app.route('/products')
def products(): return render_template('products.html')

@app.route('/blog')
def blog():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY date_posted DESC').fetchall()
    # (Same logic as before for comments/top_comment)
    posts_data = []
    for post in posts:
        post_dict = dict(post)
        comments = conn.execute('SELECT * FROM comments WHERE post_id = ? ORDER BY date_posted DESC', (post['id'],)).fetchall()
        comments_list = [dict(c) for c in comments]
        top_comment = None
        if comments_list:
            sorted_by_likes = sorted(comments_list, key=lambda x: x['likes'], reverse=True)
            if sorted_by_likes[0]['likes'] > 0:
                top_comment = sorted_by_likes[0]
        post_dict['comments'] = comments_list
        post_dict['top_comment'] = top_comment
        posts_data.append(post_dict)
    conn.close()
    return render_template('blog.html', posts=posts_data)

@app.route('/post/<int:id>')
def post(id):
    conn = get_db_connection()
    post_row = conn.execute('SELECT * FROM posts WHERE id = ?', (id,)).fetchone()
    if not post_row:
        conn.close()
        flash('Post not found!')
        return redirect(url_for('blog'))
    # (Same logic as before)
    post_dict = dict(post_row)
    comments = conn.execute('SELECT * FROM comments WHERE post_id = ? ORDER BY date_posted DESC', (id,)).fetchall()
    comments_list = [dict(c) for c in comments]
    top_comment = None
    if comments_list:
        sorted_by_likes = sorted(comments_list, key=lambda x: x['likes'], reverse=True)
        if sorted_by_likes[0]['likes'] > 0:
            top_comment = sorted_by_likes[0]
    post_dict['comments'] = comments_list
    post_dict['top_comment'] = top_comment
    conn.close()
    return render_template('post.html', post=post_dict)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('blog'))
        else:
            flash('Invalid Credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('blog'))

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if not session.get('admin_logged_in'): return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        image = request.files['image']
        filename = None
        if image and image.filename != '':
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        date_posted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content, image, date_posted) VALUES (?, ?, ?, ?)',
                     (title, content, filename, date_posted))
        conn.commit()
        conn.close()
        return redirect(url_for('blog'))
    return render_template('create_post.html')

@app.route('/edit_post/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    if not session.get('admin_logged_in'): return redirect(url_for('login'))
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (id,)).fetchone()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        image = request.files['image']
        if image and image.filename != '':
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            conn.execute('UPDATE posts SET title = ?, content = ?, image = ? WHERE id = ?',
                         (title, content, filename, id))
        else:
            conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?',
                         (title, content, id))
        conn.commit()
        conn.close()
        return redirect(url_for('blog'))
    conn.close()
    if not post:
        flash('Post not found!')
        return redirect(url_for('blog'))
    return render_template('edit_post.html', post=post)

@app.route('/delete_post/<int:id>')
def delete_post(id):
    if not session.get('admin_logged_in'): return redirect(url_for('login'))
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.execute('DELETE FROM comments WHERE post_id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('blog'))

# Standard comment route for HTML users
@app.route('/comment/<int:id>', methods=['POST'])
def add_comment(id):
    content = request.form.get('content')
    referrer = request.referrer
    if content:
        date_posted = datetime.now().strftime("%Y-%m-%d %H:%M")
        conn = get_db_connection()
        conn.execute('INSERT INTO comments (post_id, content, date_posted, likes) VALUES (?, ?, ?, 0)', (id, content, date_posted))
        conn.commit()
        conn.close()
    if referrer and f'/post/{id}' in referrer:
        return redirect(url_for('post', id=id, _anchor=f'post-{id}'))
    return redirect(url_for('blog', _anchor=f'post-{id}'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
