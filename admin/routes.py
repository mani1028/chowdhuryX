"""
Admin Panel Routes
/admin/* endpoints for dashboard, contacts, careers, blog management
"""
from datetime import datetime
from functools import wraps
from flask import render_template, request, jsonify, session, redirect, url_for, flash, current_app
from werkzeug.security import check_password_hash
from models import db, Contact, Career, Blog, Testimonial
from . import admin_bp


def login_required(f):
    """Decorator to require admin login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function


# ==================== AUTHENTICATION ====================

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Admin Login"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # In production, fetch from database
        admin_username = current_app.config.get('ADMIN_USERNAME', 'admin')
        
        if username == admin_username and password == 'admin123':  # Change this in production!
            session['admin_logged_in'] = True
            session['admin_username'] = username
            return redirect(url_for('admin.dashboard'))
        else:
            return render_template('admin/admin-login.html', error='Invalid credentials'), 401
    
    return render_template('admin/admin-login.html')


@admin_bp.route('/logout')
def logout():
    """Admin Logout"""
    session.clear()
    return redirect(url_for('admin.login'))


# ==================== DASHBOARD ====================

@admin_bp.route('/')
@admin_bp.route('/dashboard')
@login_required
def dashboard():
    """Admin Dashboard"""
    stats = {
        'total_contacts': Contact.query.count(),
        'new_contacts': Contact.query.filter_by(status='new').count(),
        'total_applications': Career.query.count(),
        'pending_applications': Career.query.filter_by(status='applied').count(),
        'total_blog_posts': Blog.query.count(),
        'draft_posts': Blog.query.filter_by(status='draft').count(),
        'total_testimonials': Testimonial.query.count(),
        'pending_testimonials': Testimonial.query.filter_by(status='pending').count()
    }
    
    recent_contacts = Contact.query.order_by(Contact.created_at.desc()).limit(5).all()
    recent_applications = Career.query.order_by(Career.created_at.desc()).limit(5).all()
    
    return render_template(
        'admin/admin-dashboard.html',
        stats=stats,
        recent_contacts=recent_contacts,
        recent_applications=recent_applications
    )


# ==================== CONTACTS ====================

@admin_bp.route('/contacts')
@login_required
def contacts():
    """View all contact submissions"""
    page = request.args.get('page', 1, type=int)
    status = request.args.get('status', 'all')
    
    query = Contact.query.order_by(Contact.created_at.desc())
    
    if status != 'all':
        query = query.filter_by(status=status)
    
    contacts = query.paginate(page=page, per_page=15)
    
    return render_template(
        'admin/admin-contacts.html',
        contacts=contacts,
        current_status=status
    )


@admin_bp.route('/contact/<int:contact_id>')
@login_required
def view_contact(contact_id):
    """View single contact"""
    contact = Contact.query.get_or_404(contact_id)
    
    if contact.status == 'new':
        contact.status = 'read'
        db.session.commit()
    
    return render_template('admin/admin-contact-detail.html', contact=contact)


@admin_bp.route('/contact/<int:contact_id>/status', methods=['POST'])
@login_required
def update_contact_status(contact_id):
    """Update contact status"""
    contact = Contact.query.get_or_404(contact_id)
    status = request.json.get('status')
    
    if status in ['new', 'read', 'resolved']:
        contact.status = status
        db.session.commit()
        return jsonify({'success': True})
    
    return jsonify({'success': False}), 400


@admin_bp.route('/contact/<int:contact_id>/delete', methods=['POST'])
@login_required
def delete_contact(contact_id):
    """Delete contact"""
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({'success': True})


# ==================== CAREERS ====================

@admin_bp.route('/careers')
@login_required
def careers():
    """View all career applications"""
    page = request.args.get('page', 1, type=int)
    status = request.args.get('status', 'all')
    
    query = Career.query.order_by(Career.created_at.desc())
    
    if status != 'all':
        query = query.filter_by(status=status)
    
    careers = query.paginate(page=page, per_page=15)
    
    return render_template(
        'admin/admin-careers.html',
        careers=careers,
        current_status=status
    )


@admin_bp.route('/career/<int:career_id>')
@login_required
def view_career(career_id):
    """View single career application"""
    career = Career.query.get_or_404(career_id)
    return render_template('admin/admin-career-detail.html', career=career)


@admin_bp.route('/career/<int:career_id>/status', methods=['POST'])
@login_required
def update_career_status(career_id):
    """Update career application status"""
    career = Career.query.get_or_404(career_id)
    status = request.json.get('status')
    rating = request.json.get('rating')
    notes = request.json.get('notes', '')
    
    if status in ['applied', 'shortlisted', 'rejected', 'hired']:
        career.status = status
    
    if rating and 1 <= int(rating) <= 5:
        career.rating = int(rating)
    
    if notes:
        career.notes = notes
    
    db.session.commit()
    return jsonify({'success': True})


@admin_bp.route('/career/<int:career_id>/delete', methods=['POST'])
@login_required
def delete_career(career_id):
    """Delete career application"""
    career = Career.query.get_or_404(career_id)
    db.session.delete(career)
    db.session.commit()
    return jsonify({'success': True})


# ==================== BLOG ====================

@admin_bp.route('/blog')
@login_required
def blog():
    """View all blog posts"""
    page = request.args.get('page', 1, type=int)
    status = request.args.get('status', 'all')
    
    query = Blog.query.order_by(Blog.created_at.desc())
    
    if status != 'all':
        query = query.filter_by(status=status)
    
    blogs = query.paginate(page=page, per_page=15)
    
    return render_template(
        'admin/admin-blog.html',
        blogs=blogs,
        current_status=status
    )


@admin_bp.route('/blog/new', methods=['GET', 'POST'])
@login_required
def create_blog():
    """Create new blog post"""
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        excerpt = request.form.get('excerpt', '')
        category = request.form.get('category', 'news')
        author = request.form.get('author', session.get('admin_username', 'Admin'))
        
        # Generate slug
        slug = title.lower().replace(' ', '-').replace('--', '-')
        
        try:
            blog = Blog(
                title=title,
                slug=slug,
                content=content,
                excerpt=excerpt,
                category=category,
                author=author,
                status='draft'
            )
            db.session.add(blog)
            db.session.commit()
            return redirect(url_for('admin.view_blog', blog_id=blog.id))
        except Exception as e:
            return render_template('admin/admin-blog-form.html', error=str(e))
    
    return render_template('admin/admin-blog-form.html')


@admin_bp.route('/blog/<int:blog_id>')
@login_required
def view_blog(blog_id):
    """View/edit blog post"""
    blog = Blog.query.get_or_404(blog_id)
    return render_template('admin/admin-blog-detail.html', blog=blog)


@admin_bp.route('/blog/<int:blog_id>/update', methods=['POST'])
@login_required
def update_blog(blog_id):
    """Update blog post"""
    blog = Blog.query.get_or_404(blog_id)
    
    blog.title = request.json.get('title', blog.title)
    blog.content = request.json.get('content', blog.content)
    blog.excerpt = request.json.get('excerpt', blog.excerpt)
    blog.category = request.json.get('category', blog.category)
    blog.status = request.json.get('status', blog.status)
    
    if blog.status == 'published' and not blog.published_at:
        blog.published_at = datetime.utcnow()
    
    blog.updated_at = datetime.utcnow()
    db.session.commit()
    
    return jsonify({'success': True})


@admin_bp.route('/blog/<int:blog_id>/delete', methods=['POST'])
@login_required
def delete_blog(blog_id):
    """Delete blog post"""
    blog = Blog.query.get_or_404(blog_id)
    db.session.delete(blog)
    db.session.commit()
    return jsonify({'success': True})
