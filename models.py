"""
Shared Database Models
Contact, Career, Job, Blog, AdminUser, Comment, Analytics models
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Contact(db.Model):
    """Contact Form Submissions"""
    __tablename__ = 'contacts'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, index=True)
    email = db.Column(db.String(120), nullable=False, index=True)
    phone = db.Column(db.String(20), nullable=True)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='new')  # new, read, resolved
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    ip_address = db.Column(db.String(45), nullable=True)
    
    def __repr__(self):
        return f'<Contact {self.name} - {self.email}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'subject': self.subject,
            'message': self.message,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }


class Career(db.Model):
    """Career Application Submissions"""
    __tablename__ = 'careers'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False, index=True)
    email = db.Column(db.String(120), nullable=False, index=True)
    phone = db.Column(db.String(20), nullable=False)
    position = db.Column(db.String(150), nullable=False, index=True)
    experience_years = db.Column(db.Integer, nullable=False)
    resume_filename = db.Column(db.String(255), nullable=True)
    cover_letter = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default='applied')  # applied, shortlisted, rejected, hired
    rating = db.Column(db.Integer, default=0)  # 1-5 stars for admin review
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    ip_address = db.Column(db.String(45), nullable=True)
    
    def __repr__(self):
        return f'<Career {self.full_name} - {self.position}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'position': self.position,
            'experience_years': self.experience_years,
            'resume_filename': self.resume_filename,
            'status': self.status,
            'rating': self.rating,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }


class Job(db.Model):
    """Job Postings"""
    __tablename__ = 'jobs'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False, index=True)
    location = db.Column(db.String(100), nullable=False)
    job_type = db.Column(db.String(50), nullable=False)  # Full-time, Part-time, Contract, Internship, Commission-based, 1099
    department = db.Column(db.String(100), nullable=True, index=True)
    experience_required = db.Column(db.String(50), nullable=False)  # e.g., "3-5 years", "5+ years"
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=True)
    responsibilities = db.Column(db.Text, nullable=True)
    salary_range = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(20), default='active')  # active, inactive, closed
    posted_by = db.Column(db.String(120), nullable=True)
    views = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    closes_at = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return f'<Job {self.title} - {self.location}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'location': self.location,
            'job_type': self.job_type,
            'department': self.department,
            'experience_required': self.experience_required,
            'description': self.description,
            'requirements': self.requirements,
            'responsibilities': self.responsibilities,
            'salary_range': self.salary_range,
            'status': self.status,
            'views': self.views,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S') if self.updated_at else None
        }


class Blog(db.Model):
    """Blog Posts"""
    __tablename__ = 'blogs'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True, index=True)
    slug = db.Column(db.String(255), nullable=False, unique=True, index=True)
    author = db.Column(db.String(120), nullable=False, default='ChowdhuryX')
    category = db.Column(db.String(50), nullable=False, default='news')
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.String(500), nullable=True)
    featured_image = db.Column(db.String(255), nullable=True)
    image_url = db.Column(db.String(500), nullable=True)  # External image URL
    video_file = db.Column(db.String(255), nullable=True)  # Uploaded video file
    video_url = db.Column(db.String(500), nullable=True)  # External video URL (YouTube, Vimeo, etc.)
    status = db.Column(db.String(20), default='draft')  # draft, published, archived
    views = db.Column(db.Integer, default=0)
    likes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published_at = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return f'<Blog {self.title}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'author': self.author,
            'category': self.category,
            'excerpt': self.excerpt,
            'featured_image': self.featured_image,
            'video_file': self.video_file,
            'video_url': self.video_url,
            'status': self.status,
            'views': self.views,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'published_at': self.published_at.strftime('%Y-%m-%d') if self.published_at else None
        }


class Testimonial(db.Model):
    """Client Testimonials"""
    __tablename__ = 'testimonials'
    
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(120), nullable=False)
    client_company = db.Column(db.String(150), nullable=True)
    client_position = db.Column(db.String(150), nullable=True)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, default=5)  # 1-5 stars
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Testimonial {self.client_name}>'


class Service(db.Model):
    """Services Offered"""
    __tablename__ = 'services'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    slug = db.Column(db.String(150), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    icon = db.Column(db.String(255), nullable=True)
    image = db.Column(db.String(255), nullable=True)
    order = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<Service {self.name}>'


class AdminUser(db.Model):
    """Admin Users for Authentication"""
    __tablename__ = 'admin_users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(150), nullable=True)
    role = db.Column(db.String(20), default='admin')  # admin, super_admin
    is_active = db.Column(db.Boolean, default=True)
    last_login = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        """Hash and set password"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verify password"""
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<AdminUser {self.username}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'full_name': self.full_name,
            'role': self.role,
            'is_active': self.is_active,
            'last_login': self.last_login.strftime('%Y-%m-%d %H:%M:%S') if self.last_login else None
        }


class Comment(db.Model):
    """Blog Post Comments"""
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id', ondelete='CASCADE'), nullable=False, index=True)
    author_name = db.Column(db.String(120), nullable=False)
    author_email = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, approved, spam, rejected
    likes = db.Column(db.Integer, default=0)
    parent_id = db.Column(db.Integer, db.ForeignKey('comments.id', ondelete='CASCADE'), nullable=True)  # For nested replies
    ip_address = db.Column(db.String(45), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    # Relationships
    blog = db.relationship('Blog', backref=db.backref('comments', lazy='dynamic', cascade='all, delete-orphan'))
    replies = db.relationship('Comment', backref=db.backref('parent', remote_side=[id]), lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Comment by {self.author_name} on Blog {self.blog_id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author_name': self.author_name,
            'content': self.content,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'replies_count': self.replies.count()
        }


class Analytics(db.Model):
    """Analytics Tracking"""
    __tablename__ = 'analytics'
    
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(50), nullable=False, index=True)  # contact, career, service_view, blog_view
    event_data = db.Column(db.String(255), nullable=True)  # service_slug, blog_slug, position_applied
    ip_address = db.Column(db.String(45), nullable=True)
    user_agent = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    def __repr__(self):
        return f'<Analytics {self.event_type}: {self.event_data}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'event_type': self.event_type,
            'event_data': self.event_data,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

