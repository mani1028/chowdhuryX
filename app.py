"""
ChowdhuryX - Corporate Website
Main Flask Application Entry Point
"""
import os
import hashlib
from dotenv import load_dotenv

# Load env vars immediately
load_dotenv()

import logging
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from functools import wraps
from config import get_config
from models import db, Contact, Career, Blog, Testimonial, Service, Job, BlogLike
try:
    from content_data_enhanced import get_service_details, get_all_services_details, get_industry_details, get_all_industries
except ImportError:
    from content_data import get_service_details, get_all_services_details, get_industry_details, get_all_industries

# Configure logging
logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize CSRF Protection
csrf = CSRFProtect()
migrate = Migrate()

def create_app(config_name=None):
    """Application Factory"""
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))
    
    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)
    
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
    
    def get_file_hash(file_obj):
        """Calculate SHA-256 hash of a file"""
        hasher = hashlib.sha256()
        file_obj.seek(0)
        while chunk := file_obj.read(8192):
            hasher.update(chunk)
        file_obj.seek(0)
        return hasher.hexdigest()
    
    def find_existing_file(file_obj, upload_dir):
        """Check if file with same content already exists in upload directory"""
        if not os.path.exists(upload_dir):
            return None
        
        file_hash = get_file_hash(file_obj)
        
        # Check all files in upload directory
        for filename in os.listdir(upload_dir):
            filepath = os.path.join(upload_dir, filename)
            if os.path.isfile(filepath):
                try:
                    with open(filepath, 'rb') as existing_file:
                        existing_hash = hashlib.sha256(existing_file.read()).hexdigest()
                        if existing_hash == file_hash:
                            return filename
                except Exception:
                    continue
        return None
    
    def save_uploaded_file(file_obj, upload_dir, file_prefix=''):
        """Save file to upload directory, reusing existing file if duplicate"""
        # Check if file already exists
        existing_filename = find_existing_file(file_obj, upload_dir)
        if existing_filename:
            logger.info(f"Reusing existing file: {existing_filename}")
            return existing_filename
        
        # Save new file with timestamp
        filename = secure_filename(file_obj.filename)
        if file_prefix:
            filename = f"{file_prefix}_{filename}"
        else:
            filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{filename}"
        
        os.makedirs(upload_dir, exist_ok=True)
        filepath = os.path.join(upload_dir, filename)
        file_obj.save(filepath)
        logger.info(f"Saved new file: {filename}")
        return filename
    
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
            logger.warning(f"Analytics tracking error: {e}")
    
    # Register blueprints
    from admin import admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    # Ensure required directories exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['BLOG_IMAGE_FOLDER'], exist_ok=True)
    os.makedirs(app.config['RESUME_FOLDER'], exist_ok=True)
    
    # Ensure database directory exists
    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    if db_uri.startswith('sqlite:///'):
        # Handle both Unix-style and Windows paths
        db_path = db_uri.replace('sqlite:///', '')
        # Normalize path separators
        db_path = db_path.replace('/', os.sep)
        db_dir = os.path.dirname(db_path)
        if db_dir:
            try:
                os.makedirs(db_dir, exist_ok=True)
            except Exception as e:
                logger.warning(f"Could not create database directory: {e}")
    
    # Create database tables (may fail on first run, will be created on demand)
    try:
        with app.app_context():
            db.create_all()
    except Exception as e:
        logger.warning(f"Database initialization warning (will retry on app startup): {e}")
    
    # Track if database has been initialized
    app.db_initialized = False
    
    @app.before_request
    def init_db():
        """Initialize database on first request if needed"""
        if not app.db_initialized:
            try:
                db.create_all()
                app.db_initialized = True
                logger.info("Database initialized successfully on first request")
            except Exception as e:
                logger.error(f"Failed to initialize database: {e}")
    
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
        """Careers Page with pagination and filters"""
        from models import Job
        
        # Get filter parameters
        job_type = request.args.get('type', '')
        department = request.args.get('department', '')
        location = request.args.get('location', '')
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        # Limit per_page to max 50
        per_page = min(per_page, 50)
        
        # Build query
        query = Job.query.filter_by(status='active')
        
        if job_type:
            query = query.filter_by(job_type=job_type)
        if department:
            query = query.filter_by(department=department)
        if location:
            query = query.filter(Job.location.ilike(f'%{location}%'))
        
        # Paginate
        jobs_pagination = query.order_by(Job.created_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        # Get unique values for filters
        all_types = db.session.query(Job.job_type).filter_by(status='active').distinct().all()
        all_departments = db.session.query(Job.department).filter_by(status='active').distinct().all()
        all_locations = db.session.query(Job.location).filter_by(status='active').distinct().all()
        
        return render_template('careers.html', 
                             jobs=jobs_pagination.items,
                             pagination=jobs_pagination,
                             job_types=[t[0] for t in all_types if t[0]],
                             departments=[d[0] for d in all_departments if d[0]],
                             locations=[l[0] for l in all_locations if l[0]],
                             current_filters={'type': job_type, 'department': department, 'location': location})
    
    @app.route('/careers/job/<int:job_id>')
    def job_detail(job_id):
        """Job Detail Page"""
        from models import Job
        
        job = Job.query.get_or_404(job_id)
        
        # Increment view count
        job.views = (job.views or 0) + 1
        db.session.commit()
        
        return render_template('job-detail.html', job=job)
    
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
                status='approved',  # Auto-approved, admin can delete if needed
                ip_address=request.remote_addr
            )
            db.session.add(comment)
            db.session.commit()
            
            return jsonify({'success': True, 'message': 'Comment posted successfully!'})
        except Exception as e:
            logger.error(f"Blog comment error: {str(e)}")
            return jsonify({'success': False, 'message': 'Error submitting comment'}), 400
    
    @app.route('/blog/<int:blog_id>/like', methods=['POST'])
    def like_blog(blog_id):
        """Like a blog post - Device-based to prevent spam"""
        try:
            blog = Blog.query.get_or_404(blog_id)
            
            # Get device ID from request
            data = request.get_json()
            device_id = data.get('device_id') if data else None
            
            if not device_id or len(device_id) < 10:
                return jsonify({'success': False, 'message': 'Invalid device identifier'}), 400
            
            # Check if this device already liked this blog
            existing_like = BlogLike.query.filter_by(blog_id=blog_id, device_id=device_id).first()
            
            if existing_like:
                return jsonify({'success': False, 'message': 'You already liked this post', 'already_liked': True}), 400
            
            # Create new like
            new_like = BlogLike(
                blog_id=blog_id,
                device_id=device_id,
                ip_address=request.remote_addr
            )
            
            # Increment blog likes counter
            if blog.likes is None:
                blog.likes = 0
            blog.likes += 1
            
            db.session.add(new_like)
            db.session.commit()
            
            return jsonify({'success': True, 'likes': blog.likes, 'liked': True})
        except Exception as e:
            logger.error(f"Blog like error: {str(e)}")
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Error liking post'}), 400
    
    @app.route('/blog/<int:blog_id>/like/check', methods=['POST'])
    def check_blog_like(blog_id):
        """Check if device has already liked this blog post"""
        try:
            # Get device ID from request
            data = request.get_json()
            device_id = data.get('device_id') if data else None
            
            if not device_id:
                return jsonify({'liked': False})
            
            # Check if this device liked this blog
            existing_like = BlogLike.query.filter_by(blog_id=blog_id, device_id=device_id).first()
            
            return jsonify({'liked': existing_like is not None})
        except Exception as e:
            logger.error(f"Check blog like error: {str(e)}")
            return jsonify({'liked': False})
    
    @app.route('/comment/<int:comment_id>/like', methods=['POST'])
    def like_comment(comment_id):
        """Like a comment"""
        try:
            from models import Comment
            comment = Comment.query.get_or_404(comment_id)
            
            # Increment likes
            if comment.likes is None:
                comment.likes = 0
            comment.likes += 1
            
            db.session.commit()
            
            return jsonify({'success': True, 'likes': comment.likes})
        except Exception as e:
            logger.error(f"Comment like error: {str(e)}")
            return jsonify({'success': False, 'message': 'Error liking comment'}), 400
    
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
                    # Use deduplication logic to save file
                    filename = save_uploaded_file(file, app.config['RESUME_FOLDER'])
                    career.resume_filename = filename
                elif file and file.filename:
                    # Invalid file extension
                    return jsonify({'success': False, 'message': f'Invalid file format. Allowed: {', '.join(app.config["ALLOWED_EXTENSIONS"])}'}), 400
            
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
    app.run(host='0.0.0.0', port=5000)
