"""
ChowdhuryX - Corporate Website
Main Flask Application Entry Point
"""
import os
import logging
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from config import get_config
from models import db, Contact, Career, Blog, Testimonial, Service

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app(config_name=None):
    """Application Factory"""
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints
    from admin import admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # ==================== PUBLIC ROUTES ====================
    
    @app.route('/')
    def index():
        """Homepage"""
        featured_blogs = Blog.query.filter_by(status='published').order_by(Blog.published_at.desc()).limit(3).all()
        services = Service.query.order_by(Service.order).all()
        testimonials = Testimonial.query.filter_by(status='approved').all()
        return render_template('index.html', blogs=featured_blogs, services=services, testimonials=testimonials)
    
    @app.route('/about')
    def about():
        """About Us Page"""
        return render_template('about.html')
    
    @app.route('/services')
    def services():
        """Services Page"""
        all_services = Service.query.order_by(Service.order).all()
        return render_template('services.html', services=all_services)
    
    @app.route('/industries')
    def industries():
        """Industries Page"""
        return render_template('industries.html')
    
    @app.route('/portfolio')
    def portfolio():
        """Portfolio/Case Studies Page"""
        return render_template('portfolio.html')
    
    @app.route('/careers')
    def careers():
        """Careers Page"""
        return render_template('careers.html')
    
    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        """Contact Us Page"""
        if request.method == 'POST':
            try:
                contact = Contact(
                    name=request.form.get('name'),
                    email=request.form.get('email'),
                    phone=request.form.get('phone', ''),
                    subject=request.form.get('subject'),
                    message=request.form.get('message'),
                    ip_address=request.remote_addr,
                    status='new'
                )
                db.session.add(contact)
                db.session.commit()
                return jsonify({'success': True, 'message': 'Thank you for contacting us. We will get back to you soon.'})
            except Exception as e:
                logger.error(f"Contact form error: {str(e)}")
                return jsonify({'success': False, 'message': 'Error submitting form'}), 400
        
        return render_template('contact.html')
    
    @app.route('/blog')
    def blog():
        """Blog Listing Page"""
        page = request.args.get('page', 1, type=int)
        blogs = Blog.query.filter_by(status='published').order_by(Blog.published_at.desc()).paginate(page=page, per_page=10)
        return render_template('blog.html', blogs=blogs)
    
    @app.route('/blog/<slug>')
    def blog_post(slug):
        """Blog Post Detail Page"""
        blog = Blog.query.filter_by(slug=slug).first_or_404()
        blog.views += 1
        db.session.commit()
        related_blogs = Blog.query.filter_by(status='published', category=blog.category).filter(Blog.id != blog.id).limit(3).all()
        return render_template('blog-post.html', blog=blog, related_blogs=related_blogs)
    
    @app.route('/faq')
    def faq():
        """FAQ Page"""
        return render_template('faq.html')
    
    @app.route('/testimonials')
    def testimonials():
        """Testimonials Page"""
        approved_testimonials = Testimonial.query.filter_by(status='approved').all()
        return render_template('testimonials.html', testimonials=approved_testimonials)
    
    @app.route('/privacy-policy')
    def privacy_policy():
        """Privacy Policy Page"""
        return render_template('privacy-policy.html')
    
    @app.route('/terms')
    def terms():
        """Terms of Service Page"""
        return render_template('terms.html')
    
    @app.route('/cookies')
    def cookies():
        """Cookie Policy Page"""
        return render_template('cookies.html')
    
    @app.route('/apply-job', methods=['POST'])
    def apply_job():
        """Career Application Submission"""
        try:
            career = Career(
                full_name=request.form.get('full_name'),
                email=request.form.get('email'),
                phone=request.form.get('phone'),
                position=request.form.get('position'),
                experience_years=int(request.form.get('experience_years', 0)),
                cover_letter=request.form.get('cover_letter', ''),
                ip_address=request.remote_addr,
                status='applied'
            )
            
            # Handle file upload
            if 'resume' in request.files:
                file = request.files['resume']
                if file and file.filename:
                    filename = f"{datetime.now().timestamp()}_{file.filename}"
                    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    career.resume_filename = filename
            
            db.session.add(career)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Application submitted successfully!'})
        except Exception as e:
            logger.error(f"Job application error: {str(e)}")
            return jsonify({'success': False, 'message': 'Error submitting application'}), 400
    
    # ==================== ERROR HANDLERS ====================
    
    @app.errorhandler(404)
    def not_found_error(error):
        """404 Error Handler"""
        return render_template('404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """500 Error Handler"""
        logger.error(f"Server error: {error}")
        db.session.rollback()
        return render_template('500.html'), 500
    
    # ==================== CONTEXT PROCESSORS ====================
    
    @app.context_processor
    def inject_config():
        """Inject config variables into templates"""
        return {
            'current_year': datetime.now().year,
            'company_name': 'ChowdhuryX',
            'company_email': 'info@chowdhuryX.com',
            'company_phone': '+1 (555) 123-4567'
        }
    
    # ==================== TEMPLATE FILTERS ====================
    
    @app.template_filter('datetime_format')
    def datetime_format(value, format_str='%B %d, %Y'):
        """Format datetime in templates"""
        if isinstance(value, datetime):
            return value.strftime(format_str)
        return value
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
