from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, send_from_directory
import sqlite3
import os
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_change_this'  # Change this to a random secret key

# --- CPANEL FIX: Use Absolute Paths ---
# 1. Get the absolute path of the directory where app.py is located
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# 2. Update configuration to use absolute paths based on BASE_DIR
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static/uploads')
app.config['DATABASE'] = os.path.join(BASE_DIR, 'database.db')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Admin Credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"

def get_db_connection():
    # Use the absolute path config
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    # Create posts table
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
    # Create comments table
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
        print("Migrated: Added 'likes' column to comments table.")

    conn.commit()
    conn.close()

# Initialize DB on start
with app.app_context():
    init_db()

# --- SEO ROUTES (Robots & Sitemap) ---
@app.route('/robots.txt')
def robots():
    # Serve robots.txt from the same directory as app.py
    return send_from_directory(BASE_DIR, 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    # Serve sitemap.xml from the same directory as app.py
    return send_from_directory(BASE_DIR, 'sitemap.xml')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/blog')
def blog():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY date_posted DESC').fetchall()
    
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
    
    if post_row is None:
        conn.close()
        flash('Post not found!')
        return redirect(url_for('blog'))

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
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))

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
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    
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
    if post is None:
        flash('Post not found!')
        return redirect(url_for('blog'))
        
    return render_template('edit_post.html', post=post)

@app.route('/delete_post/<int:id>')
def delete_post(id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.execute('DELETE FROM comments WHERE post_id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('blog'))

@app.route('/like/<int:id>', methods=['POST'])
def like_post(id):
    liked_cookie = request.cookies.get(f'liked_post_{id}')
    
    conn = get_db_connection()
    if not liked_cookie:
        conn.execute('UPDATE posts SET likes = likes + 1 WHERE id = ?', (id,))
        conn.commit()
    
    post = conn.execute('SELECT likes FROM posts WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    response = jsonify({'likes': post['likes'], 'status': 'success' if not liked_cookie else 'already_liked'})
    if not liked_cookie:
        response.set_cookie(f'liked_post_{id}', 'true', max_age=31536000)
        
    return response

@app.route('/like_comment/<int:id>', methods=['POST'])
def like_comment(id):
    liked_cookie = request.cookies.get(f'liked_comment_{id}')
    
    conn = get_db_connection()
    if not liked_cookie:
        conn.execute('UPDATE comments SET likes = likes + 1 WHERE id = ?', (id,))
        conn.commit()
    
    comment = conn.execute('SELECT likes FROM comments WHERE id = ?', (id,)).fetchone()
    conn.close()

    response = jsonify({'likes': comment['likes']})
    if not liked_cookie:
        response.set_cookie(f'liked_comment_{id}', 'true', max_age=31536000)
    
    return response

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

if __name__ == '__main__':
    app.run(debug=True)