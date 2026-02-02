"""
Create Admin User Script
Run this to create/update the admin user with credentials from .env
Usage: python create_admin.py
"""
import os
from dotenv import load_dotenv

# CRITICAL: Load environment variables BEFORE importing app or config
# This ensures DATABASE_URL is available when config.py is read
load_dotenv()

from app import create_app
from models import db, AdminUser

def create_admin():
    """Create/update admin user from .env credentials"""
    app = create_app()
    
    with app.app_context():
        # Drop and recreate all tables to ensure schema is up to date
        print("Updating database schema...")
        db.drop_all()
        db.create_all()
        print("✓ Database tables created")
        
        # Get admin credentials from .env
        admin_username = os.getenv('ADMIN_USERNAME', 'admin')
        admin_password = os.getenv('ADMIN_PASSWORD', 'admin123')
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

if __name__ == '__main__':
    create_admin()
