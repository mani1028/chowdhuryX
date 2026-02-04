"""
Create Admin User Script
Run this to create/update the admin user with credentials from .env
Usage: python create_admin.py
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# CRITICAL: Load environment variables BEFORE importing app or config
# This ensures DATABASE_URL is available when config.py is read
load_dotenv()

from app import create_app
from models import db, AdminUser

def create_admin():
    """Create/update admin user from .env credentials"""
    try:
        app = create_app()
    except Exception as e:
        print(f"❌ Error creating app: {e}")
        print("\nTrying to fix database path...")
        sys.exit(1)
    
    with app.app_context():
        try:
            # Ensure database directory exists
            db_uri = app.config['SQLALCHEMY_DATABASE_URI']
            if db_uri.startswith('sqlite:///'):
                db_path = db_uri.replace('sqlite:///', '').replace('/', os.sep)
                db_dir = os.path.dirname(db_path)
                if db_dir:
                    os.makedirs(db_dir, exist_ok=True)
            
            # Drop and recreate all tables to ensure schema is up to date
            print("\nUpdating database schema...")
            db.drop_all()
            db.create_all()
            print("✓ Database tables created")
        except Exception as e:
            print(f"❌ Error creating database tables: {e}")
            sys.exit(1)
        
        try:
            # Get admin credentials from .env
            admin_username = os.getenv('ADMIN_USERNAME', 'chowdhuryx')
            admin_password = os.getenv('ADMIN_PASSWORD', 'chowdhuryx123')
            admin_email = os.getenv('ADMIN_EMAIL', 'admin@chowdhuryx.com')
            
            # Create new admin user
            admin = AdminUser(
                username=admin_username,
                email=admin_email,
                full_name='System Administrator',
                role='super_admin',
                is_active=True
            )
            admin.set_password(admin_password)  # Password is hashed automatically
            
            db.session.add(admin)
            db.session.commit()
            
            print("\n✓ Admin user created successfully!")
            print("=" * 60)
            print(f"  Username: {admin_username}")
            print(f"  Password: {admin_password} (from .env file)")
            print(f"  Email: {admin_email}")
            print(f"  Role: super_admin")
            print("=" * 60)
            print("\n📝 TO CHANGE ADMIN CREDENTIALS:")
            print("   1. Edit .env file:")
            print(f"      ADMIN_USERNAME={admin_username}")
            print(f"      ADMIN_PASSWORD={admin_password}")
            print(f"      ADMIN_EMAIL={admin_email}")
            print("   2. Run: python create_admin.py")
            print("   3. Database will be updated automatically!")
            print("\n⚠️  For production, change SECRET_KEY in .env!")
        except Exception as e:
            print(f"❌ Error creating admin user: {e}")
            sys.exit(1)

if __name__ == '__main__':
    create_admin()
