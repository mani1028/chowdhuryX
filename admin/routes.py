"""
Admin Panel Routes - Enhanced Version
Handles: Authentication, Dashboard, Contacts, Careers, Blog, Comments, Analytics, Export, Email Notifications
"""
import os
import csv
import io
from datetime import datetime
from functools import wraps
from flask import render_template, request, jsonify, session, redirect, url_for, flash, current_app, send_file
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from models import db, Contact, Career, Blog, Testimonial, AdminUser, Comment, Analytics
from . import admin_bp

# Optional Flask-Mail import
try:
    from flask_mail import Mail, Message
    mail = Mail()
    HAS_MAIL = True
except ImportError:
    HAS_MAIL = False
    print("⚠️  Flask-Mail not installed. Email notifications will be disabled.")

def login_required(f):
    """Decorator to require admin login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_id' not in session:
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function


def role_required(role):
    """Decorator to check admin role"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'admin_id' not in session:
                return redirect(url_for('admin.login'))
            admin = AdminUser.query.get(session['admin_id'])
            if not admin or admin.role not in ['admin', role]:
                return jsonify({'error': 'Insufficient permissions'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def send_email(subject, recipients, text_body, html_body=None):
    """Send email notification"""
    if not HAS_MAIL or not current_app.config.get('MAIL_USERNAME'):
        current_app.logger.info(f"Email notification (disabled): {subject}")
        return False
    
    try:
        msg = Message(
            subject=subject,
            recipients=recipients,
            body=text_body,
            html=html_body
        )
        mail.send(msg)
        return True
    except Exception as e:
        current_app.logger.error(f"Email error: {e}")
        return False


# ==================== AUTHENTICATION ====================

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Admin Login with Database Authentication"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        admin = AdminUser.query.filter_by(username=username, is_active=True).first()
        
        if admin and admin.check_password(password):
            session['admin_logged_in'] = True
            session['admin_id'] = admin.id
            session['admin_username'] = admin.username
            session['admin_role'] = admin.role
            
            # Update last login
            admin.last_login = datetime.utcnow()
            db.session.commit()
            
            flash(f'Welcome back, {admin.full_name or admin.username}!', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid username or password', 'error')
            return render_template('admin-login.html', error='Invalid credentials'), 401
    
    return render_template('admin-login.html')


@admin_bp.route('/logout')
def logout():
    """Admin Logout"""
    session.clear()
    flash('Logged out successfully', 'success')
    return redirect(url_for('admin.login'))


# ==================== DASHBOARD ====================

@admin_bp.route('/')
@admin_bp.route('/dashboard')
@login_required
def dashboard():
    """Admin Dashboard with Statistics and Analytics"""
    stats = {
        'total_contacts': Contact.query.count(),
        'new_contacts': Contact.query.filter_by(status='new').count(),
        'total_applications': Career.query.count(),
        'pending_applications': Career.query.filter_by(status='applied').count(),
        'total_blog_posts': Blog.query.count(),
        'draft_posts': Blog.query.filter_by(status='draft').count(),
        'total_testimonials': Testimonial.query.count(),
        'pending_testimonials': Testimonial.query.filter_by(status='pending').count(),
        'pending_comments': Comment.query.filter_by(status='pending').count(),
        'total_comments': Comment.query.count(),
    }
    
    recent_contacts = Contact.query.order_by(Contact.created_at.desc()).limit(5).all()
    recent_applications = Career.query.order_by(Career.created_at.desc()).limit(5).all()
    pending_comments = Comment.query.filter_by(status='pending').limit(5).all()
    
    # Top Services (most viewed from analytics)
    top_services = db.session.execute(
        db.text("""
            SELECT event_data as service_name, COUNT(*) as view_count 
            FROM analytics 
            WHERE event_type = 'service_view' AND event_data IS NOT NULL
            GROUP BY event_data
            ORDER BY view_count DESC 
            LIMIT 5
        """)
    ).fetchall()
    
    # Popular Positions (most applications)
    popular_positions = Career.query.with_entities(
        Career.position, 
        db.func.count(Career.id).label('count')
    ).group_by(Career.position).order_by(db.desc(db.func.count(Career.id))).limit(5).all()
    
    return render_template(
        'admin-dashboard.html',
        stats=stats,
        recent_contacts=recent_contacts,
        recent_applications=recent_applications,
        pending_comments=pending_comments,
        top_services=top_services,
        popular_positions=popular_positions
    )


# ==================== CONTACTS ====================

@admin_bp.route('/contacts')
@login_required
def contacts():
    """View all contact submissions with export"""
    page = request.args.get('page', 1, type=int)
    status = request.args.get('status', 'all')
    export = request.args.get('export', 'false').lower() == 'true'
    
    query = Contact.query.order_by(Contact.created_at.desc())
    
    if status != 'all':
        query = query.filter_by(status=status)
    
    if export:
        return export_contacts_csv(query.all())
    
    contacts = query.paginate(page=page, per_page=15)
    
    return render_template(
        'admin-contacts.html',
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
    
    return render_template('admin-contact-detail.html', contact=contact)


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


def export_contacts_csv(contacts):
    """Export contacts to CSV"""
    output = io.StringIO()
    writer = csv.writer(output)
    
    writer.writerow(['Name', 'Email', 'Phone', 'Subject', 'Status', 'Date', 'Message'])
    for contact in contacts:
        writer.writerow([
            contact.name,
            contact.email,
            contact.phone or '',
            contact.subject,
            contact.status,
            contact.created_at.strftime('%Y-%m-%d %H:%M'),
            contact.message[:100]
        ])
    
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'contacts_{datetime.now().strftime("%Y%m%d")}.csv'
    )


# ==================== CAREERS ====================

@admin_bp.route('/careers')
@login_required
def careers():
    """View all career applications with export"""
    page = request.args.get('page', 1, type=int)
    status = request.args.get('status', 'all')
    export = request.args.get('export', 'false').lower() == 'true'
    
    query = Career.query.order_by(Career.created_at.desc())
    
    if status != 'all':
        query = query.filter_by(status=status)
    
    if export:
        return export_careers_csv(query.all())
    
    careers = query.paginate(page=page, per_page=15)
    
    return render_template(
        'admin-careers.html',
        careers=careers,
        current_status=status
    )


@admin_bp.route('/career/<int:career_id>')
@login_required
def view_career(career_id):
    """View single career application"""
    career = Career.query.get_or_404(career_id)
    return render_template('admin-career-detail.html', career=career)


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


def export_careers_csv(careers):
    """Export career applications to CSV"""
    output = io.StringIO()
    writer = csv.writer(output)
    
    writer.writerow(['Name', 'Email', 'Position', 'Experience', 'Status', 'Rating', 'Date'])
    for career in careers:
        writer.writerow([
            career.full_name,
            career.email,
            career.position,
            f'{career.experience_years} years',
            career.status,
            f'{career.rating}/5' if career.rating else 'Not rated',
            career.created_at.strftime('%Y-%m-%d %H:%M')
        ])
    
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'careers_{datetime.now().strftime("%Y%m%d")}.csv'
    )


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
        'admin-blog.html',
        blogs=blogs,
        current_status=status
    )


@admin_bp.route('/blog/new', methods=['GET', 'POST'])
@login_required
def create_blog():
    """Create new blog post with image upload"""
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        excerpt = request.form.get('excerpt', '')
        category = request.form.get('category', 'news')
        author = request.form.get('author', session.get('admin_username', 'Admin'))
        
        # Handle featured image upload
        featured_image = None
        if 'featured_image' in request.files:
            file = request.files['featured_image']
            if file and allowed_file(file.filename, 'image'):
                filename = secure_filename(file.filename)
                filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{filename}"
                file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
                featured_image = filename
        
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
                featured_image=featured_image,
                status='draft'
            )
            db.session.add(blog)
            db.session.commit()
            flash('Blog post created successfully', 'success')
            return redirect(url_for('admin.view_blog', blog_id=blog.id))
        except Exception as e:
            flash(f'Error creating blog: {str(e)}', 'error')
            return render_template('admin-blog-form.html', error=str(e))
    
    return render_template('admin-blog-form.html')


@admin_bp.route('/blog/<int:blog_id>')
@login_required
def view_blog(blog_id):
    """View/edit blog post"""
    blog = Blog.query.get_or_404(blog_id)
    comments = Comment.query.filter_by(blog_id=blog_id).all()
    return render_template('admin-blog-detail.html', blog=blog, comments=comments)


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


@admin_bp.route('/blog/<int:blog_id>/publish', methods=['POST'])
@login_required
def publish_blog(blog_id):
    """Publish blog post (change status from draft to published)"""
    blog = Blog.query.get_or_404(blog_id)
    
    if blog.status == 'draft':
        blog.status = 'published'
        blog.published_at = datetime.utcnow()
        db.session.commit()
        return jsonify({'success': True, 'message': 'Blog published successfully'})
    
    return jsonify({'success': False, 'message': 'Blog is already published'}), 400


@admin_bp.route('/blog/<int:blog_id>/unpublish', methods=['POST'])
@login_required
def unpublish_blog(blog_id):
    """Unpublish blog post (change status from published to draft)"""
    blog = Blog.query.get_or_404(blog_id)
    
    if blog.status == 'published':
        blog.status = 'draft'
        blog.published_at = None
        db.session.commit()
        return jsonify({'success': True, 'message': 'Blog unpublished successfully'})
    
    return jsonify({'success': False, 'message': 'Blog is already draft'}), 400


# ==================== COMMENTS ====================

@admin_bp.route('/comments')
@login_required
def comments():
    """View all comments pending moderation"""
    page = request.args.get('page', 1, type=int)
    status = request.args.get('status', 'pending')
    
    query = Comment.query.order_by(Comment.created_at.desc())
    
    if status != 'all':
        query = query.filter_by(status=status)
    
    comments = query.paginate(page=page, per_page=15)
    
    return render_template(
        'admin-comments.html',
        comments=comments,
        current_status=status
    )


@admin_bp.route('/comment/<int:comment_id>/approve', methods=['POST'])
@login_required
def approve_comment(comment_id):
    """Approve comment"""
    comment = Comment.query.get_or_404(comment_id)
    comment.status = 'approved'
    comment.approved_at = datetime.utcnow()
    db.session.commit()
    
    # Send email notification
    if current_app.config.get('EMAIL_ON_NEW_COMMENT'):
        send_email(
            subject=f'Comment Approved on "{comment.blog.title}"',
            recipients=[comment.author_email],
            text_body=f'Your comment has been approved and is now visible on the blog.'
        )
    
    return jsonify({'success': True, 'status': 'approved'})


@admin_bp.route('/comment/<int:comment_id>/reject', methods=['POST'])
@login_required
def reject_comment(comment_id):
    """Reject comment"""
    comment = Comment.query.get_or_404(comment_id)
    comment.status = 'rejected'
    db.session.commit()
    
    return jsonify({'success': True, 'status': 'rejected'})


@admin_bp.route('/comment/<int:comment_id>/spam', methods=['POST'])
@login_required
def mark_spam(comment_id):
    """Mark comment as spam"""
    comment = Comment.query.get_or_404(comment_id)
    comment.status = 'spam'
    db.session.commit()
    
    return jsonify({'success': True, 'status': 'spam'})


@admin_bp.route('/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    """Delete comment"""
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    
    return jsonify({'success': True})


# ==================== ANALYTICS ====================

@admin_bp.route('/analytics')
@login_required
def analytics():
    """View analytics and statistics"""
    # Top services (most viewed)
    top_services = db.session.execute(
        db.text("""
            SELECT event_data as service_name, COUNT(*) as count
            FROM analytics
            WHERE event_type = 'service_view' AND event_data IS NOT NULL
            GROUP BY event_data
            ORDER BY count DESC
            LIMIT 10
        """)
    ).fetchall()
    
    # Top positions (most applied)
    top_positions = db.session.execute(
        db.text("""
            SELECT event_data as position_name, COUNT(*) as count
            FROM analytics
            WHERE event_type = 'career_application' AND event_data IS NOT NULL
            GROUP BY event_data
            ORDER BY count DESC
            LIMIT 10
        """)
    ).fetchall()
    
    # Contacts over time (last 30 days)
    from datetime import timedelta
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    
    daily_contacts = db.session.execute(
        db.text("""
            SELECT DATE(created_at) as date, COUNT(*) as count
            FROM contacts
            WHERE created_at >= :date
            GROUP BY DATE(created_at)
            ORDER BY date DESC
        """),
        {'date': thirty_days_ago}
    ).fetchall()
    
    return render_template(
        'admin-analytics.html',
        top_services=top_services,
        top_positions=top_positions,
        daily_contacts=daily_contacts
    )


# ==================== UTILITY FUNCTIONS ====================

def allowed_file(filename, file_type='file'):
    """Check if file is allowed"""
    if '.' not in filename:
        return False
    
    ext = filename.rsplit('.', 1)[1].lower()
    
    if file_type == 'image':
        return ext in current_app.config['ALLOWED_IMAGE_EXTENSIONS']
    else:
        return ext in current_app.config['ALLOWED_EXTENSIONS']


def track_service_contact(service_name):
    """Track contact for a service"""
    analytics = Analytics(
        event_type='service_view',
        event_data=service_name,
        ip_address=request.remote_addr,
        user_agent=request.headers.get('User-Agent')
    )
    db.session.add(analytics)
    db.session.commit()


def track_position_application(position_name):
    """Track application for a position"""
    analytics = Analytics(
        event_type='career_application',
        event_data=position_name,
        ip_address=request.remote_addr,
        user_agent=request.headers.get('User-Agent')
    )
    db.session.add(analytics)
    db.session.commit()


def send_admin_notification(subject, message, email_type='contact'):
    """Send email notification to admin"""
    admin_emails = current_app.config.get('ADMIN_EMAILS', [])
    
    if not admin_emails:
        return False
    
    # Send to first admin email (primary admin)
    recipient = admin_emails[0] if isinstance(admin_emails, list) else admin_emails
    
    send_email(
        subject=subject,
        recipients=[recipient],
        text_body=message,
        html_body=f'<p>{message}</p>'
    )
    
    return True
