"""
Application Configuration
Handles environment-based configuration for development and production
"""
import os
from datetime import timedelta
import tempfile

def _get_db_uri():
    """Get database URI - PostgreSQL for production, SQLite for development"""
    db_uri = os.getenv('DATABASE_URL')
    if db_uri:
        return db_uri
    
    # Development: SQLite
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_dir = os.path.join(basedir, 'instance')
    try:
        os.makedirs(db_dir, exist_ok=True)
        db_file = os.path.join(db_dir, 'chowdhuryX.db')
        db_file_forward = db_file.replace('\\', '/')
        return f'sqlite:///{db_file_forward}'
    except Exception:
        db_file = os.path.join(tempfile.gettempdir(), 'chowdhuryX', 'chowdhuryX.db')
        os.makedirs(os.path.dirname(db_file), exist_ok=True)
        db_file_forward = db_file.replace('\\', '/')
        return f'sqlite:///{db_file_forward}'

class Config:
    """Base configuration"""
    # Flask Settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-this-in-production-with-strong-key')
    DEBUG = False
    TESTING = False
    
    # Database
    SQLALCHEMY_DATABASE_URI = _get_db_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 3600,
    }
    
    # Session
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Upload Settings
    # Keep this >= largest allowed upload to avoid request-level rejections.
    MAX_CONTENT_LENGTH = 120 * 1024 * 1024  # 120MB max request size
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static/uploads')
    BLOG_IMAGE_FOLDER = os.path.join(os.path.dirname(__file__), 'static/uploads/blog')
    RESUME_FOLDER = os.path.join(os.path.dirname(__file__), 'static/uploads/resumes')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'doc', 'docx'}
    ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

    # Blog Limits
    BLOG_IMAGE_MAX_BYTES = 5 * 1024 * 1024  # 5MB
    BLOG_VIDEO_MAX_BYTES = 100 * 1024 * 1024  # 100MB
    BLOG_CONTENT_MAX_CHARS = 100000
    BLOG_EXCERPT_MAX_CHARS = 500
    BLOG_TITLE_MAX_CHARS = 255
    
    # Email Configuration
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'true').lower() == 'true'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', '')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', '')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@chowdhuryx.com')
    
    # Admin Notification Emails
    ADMIN_EMAILS = os.getenv('ADMIN_EMAILS', 'admin@chowdhuryx.com').split(',')
    NOTIFY_ON_CONTACT = os.getenv('NOTIFY_ON_CONTACT', 'true').lower() == 'true'
    NOTIFY_ON_APPLICATION = os.getenv('NOTIFY_ON_APPLICATION', 'true').lower() == 'true'
    
    # Pagination
    ITEMS_PER_PAGE = 10
    
    # Security
    JSON_SORT_KEYS = False
    PREFERRED_URL_SCHEME = 'https'
    PROPAGATE_EXCEPTIONS = False


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SESSION_COOKIE_SECURE = False
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SESSION_COOKIE_SECURE = True


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


# Select config based on environment
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

def get_config(env=None):
    """Get configuration object"""
    if env is None:
        env = os.getenv('FLASK_ENV', 'development')
    return config.get(env, config['default'])
