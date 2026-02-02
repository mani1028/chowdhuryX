"""
ChowdhuryX - Corporate Website
Main Flask Application Entry Point
"""
import os
from dotenv import load_dotenv

# Load env vars immediately
load_dotenv()

import logging
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from functools import wraps
from config import get_config
from models import db, Contact, Career, Blog, Testimonial, Service
try:
    from content_data_enhanced import get_service_details, get_all_services_details, get_industry_details, get_all_industries
except ImportError:
    from content_data import get_service_details, get_all_services_details, get_industry_details, get_all_industries

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize CSRF Protection
csrf = CSRFProtect()

def create_app(config_name=None):
    """Application Factory"""
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))
    
    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)
    
    # Helper function for file validation
    def allowed_file(filename, file_type='file'):
        """Check if file has allowed extension"""
        if '.' not in filename:
            return False
        ext = filename.rsplit('.', 1)[1].lower()
        if file_type == 'resume':
            return ext in app.config['ALLOWED_EXTENSIONS']
        elif file_type == 'image':
            return ext in app.config['ALLOWED_IMAGE_EXTENSIONS']
        else:
            return ext in app.config['ALLOWED_EXTENSIONS']
    
    # Helper function to track service views for analytics
    def track_service_view(slug):
        """Track service page view in analytics"""
        try:
            from models import Analytics
            analytics = Analytics(
                event_type='service_view',
                event_data=slug,
                ip_address=request.remote_addr,
                user_agent=request.headers.get('User-Agent', '')
            )
            db.session.add(analytics)
            db.session.commit()
        except Exception as e:
            logger.debug(f"Analytics tracking error: {e}")
    
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
        """Services Page - Modern grid with detail pages"""
        service_details = get_all_services_details()
        
        # Convert service details to list format for template
        services_list = []
        for slug, details in service_details.items():
            service_data = {
                'slug': slug,
                'name': details.get('name', ''),
                'tagline': details.get('tagline', ''),
                'icon': details.get('icon', 'fas fa-cog'),
                'color': details.get('color', '#10b981'),
                'description': details.get('description', ''),
                'short_description': details.get('short_description', details.get('description', '')),
                'full_description': details.get('full_description', ''),
                'features': details.get('features', []),
                'technologies': details.get('technologies', []),
                'benefits': details.get('benefits', []),
                'pricing': details.get('pricing', 'Custom pricing'),
            }
            services_list.append(service_data)
        
        return render_template('services.html', services=services_list, service_details=service_details)
    
    @app.route('/services/<slug>')
    def service_detail(slug):
        """Individual Service Detail Page"""
        # Track service view for analytics
        track_service_view(slug)
        
        # First try to get from content_data
        details = get_service_details(slug)
        
        if not details:
            # Fallback to database
            service = Service.query.filter_by(slug=slug).first_or_404()
            details = {
                'name': service.name,
                'description': service.description,
                'full_description': service.description,
                'benefits': [],
                'technologies': [],
                'keywords': '',
                'slug': service.slug
            }
        
        # Create service object from details
        class ServiceDetail:
            def __init__(self, details):
                self.name = details.get('name', '')
                self.description = details.get('description', '')
                self.slug = details.get('slug', '')
                self.icon = details.get('icon', 'fas fa-cog')
                self.color = details.get('color', '#10b981')
        
        service = ServiceDetail(details)
        
        # Pass SEO metadata
        description = details.get('seo_description', details.get('description', ''))
        keywords = details.get('seo_keywords', details.get('keywords', ''))
        
        return render_template('service-detail.html', service=service, details=details, 
                             seo_description=description, seo_keywords=keywords)
    
    @app.route('/industries')
    def industries():
        """Industries Page"""
        return render_template('industries.html')
    
    @app.route('/industries/<slug>')
    def industry_detail(slug):
        """Individual Industry Detail Page"""
        industry = get_industry_details(slug)
        if not industry:
            return render_template('404.html'), 404
        
        return render_template('industry-detail.html', industry=industry, slug=slug)
    
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
        """Contact Us Page - with optional service pre-population"""
        service_slug = request.args.get('service', None)
        service_name = ''
        
        if service_slug:
            service_details = get_service_details(service_slug)
            service_name = service_details.get('name', '') if service_details else ''
        
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
        
        return render_template('contact.html', service_name=service_name, service_slug=service_slug)
    
    @app.route('/blog')
    def blog():
        """Blog Listing Page"""
        page = request.args.get('page', 1, type=int)
        blogs = Blog.query.filter_by(status='published').order_by(Blog.published_at.desc()).paginate(page=page, per_page=10)
        return render_template('blog.html', blogs=blogs)
    
    @app.route('/blog/<slug>')
    def blog_post(slug):
        """Blog Post Detail Page"""
        blog = Blog.query.filter_by(slug=slug, status='published').first_or_404()
        blog.views += 1
        db.session.commit()
        related_blogs = Blog.query.filter_by(status='published', category=blog.category).filter(Blog.id != blog.id).limit(3).all()
        return render_template('blog-post.html', blog=blog, related_blogs=related_blogs)
    
    @app.route('/blog/<int:blog_id>/comment', methods=['POST'])
    def add_blog_comment(blog_id):
        """Add comment to blog post (No login required)"""
        try:
            blog = Blog.query.get_or_404(blog_id)
            author_name = request.form.get('author_name', '').strip()
            author_email = request.form.get('author_email', '').strip()
            content = request.form.get('content', '').strip()
            
            if not all([author_name, author_email, content]):
                return jsonify({'success': False, 'message': 'All fields are required'}), 400
            
            if len(content) > 1000:
                return jsonify({'success': False, 'message': 'Comment is too long (max 1000 characters)'}), 400
            
            # Import Comment model
            from models import Comment
            
            comment = Comment(
                blog_id=blog_id,
                author_name=author_name,
                author_email=author_email,
                content=content,
                status='pending',  # Requires admin approval
                ip_address=request.remote_addr
            )
            db.session.add(comment)
            db.session.commit()
            
            return jsonify({'success': True, 'message': 'Comment submitted for approval'})
        except Exception as e:
            logger.error(f"Blog comment error: {str(e)}")
            return jsonify({'success': False, 'message': 'Error submitting comment'}), 400
    
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
    
    @app.route('/engagement-models')
    def engagement_models():
        """Engagement Models Page"""
        return render_template('engagement-models.html')
    
    @app.route('/why-choose-us')
    def why_choose_us():
        """Why Choose Us Page"""
        return render_template('why-choose-us.html')
    
    @app.route('/trust-center')
    def trust_center():
        """Trust Center Page"""
        return render_template('trust-center.html')
    
    @app.route('/cookie-settings')
    def cookie_settings():
        """Cookie Settings Page"""
        return render_template('cookie-settings.html')
    
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
            
            # Handle file upload with validation
            if 'resume' in request.files:
                file = request.files['resume']
                if file and file.filename and allowed_file(file.filename, 'resume'):
                    # Sanitize filename using secure_filename
                    original_filename = secure_filename(file.filename)
                    filename = f"{datetime.now().timestamp()}_{original_filename}"
                    os.makedirs(app.config['RESUME_FOLDER'], exist_ok=True)
                    file.save(os.path.join(app.config['RESUME_FOLDER'], filename))
                    career.resume_filename = filename
                elif file and file.filename:
                    # Invalid file extension
                    return jsonify({'success': False, 'message': f'Invalid file format. Allowed: {", ".join(app.config["ALLOWED_EXTENSIONS"])}'}), 400
            
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
        from flask_wtf.csrf import generate_csrf
        return {
            'current_year': datetime.now().year,
            'company_name': 'ChowdhuryX',
            'company_email': 'info@chowdhuryX.com',
            'company_phone': '+1 (555) 123-4567',
            'csrf_token': generate_csrf
        }
    
    # ==================== CLI COMMANDS ====================
    
    @app.cli.command()
    def init_services():
        """Initialize database with sample services"""
        services_data = [
            Service(
                name='Software Development',
                slug='software-development',
                description='Custom software engineering solutions for web, mobile, desktop, and enterprise applications using modern, scalable architectures.',
                order=1
            ),
            Service(
                name='AI & Machine Learning',
                slug='ai-machine-learning',
                description='Custom AI systems, automation platforms, data-driven intelligence, and advanced analytics for smarter decision-making.',
                order=2
            ),
            Service(
                name='BPO Services',
                slug='bpo-services',
                description='High-quality voice and non-voice support, CRM-driven chat operations, and customer engagement services.',
                order=3
            ),
            Service(
                name='IT Consulting',
                slug='it-consulting',
                description='Strategic IT consulting and technical architecture services for organizational transformation and digital strategy.',
                order=4
            ),
            Service(
                name='RPO & Staffing',
                slug='rpo-staffing',
                description='Recruitment Process Outsourcing and staffing solutions for building and scaling your team with qualified professionals.',
                order=5
            ),
            Service(
                name='Digital Products',
                slug='digital-products',
                description='Building scalable digital products from concept to market, with focus on user experience and business impact.',
                order=6
            ),
        ]
        
        # Check if services already exist
        existing = Service.query.first()
        if existing:
            logger.info("Services already initialized")
            return
        
        for service in services_data:
            db.session.add(service)
        
        db.session.commit()
        logger.info(f"Initialized {len(services_data)} services")
        print(f"✓ Successfully initialized {len(services_data)} services")
    
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
