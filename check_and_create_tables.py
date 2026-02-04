"""
Quick script to check database tables and create them if needed
Usage: python check_and_create_tables.py
"""
import os
from app import create_app, db
from sqlalchemy import inspect, text

def check_and_create_tables():
    """Check existing tables and create missing ones"""
    app = create_app(os.getenv('FLASK_ENV', 'development'))
    
    with app.app_context():
        # Get database engine
        engine = db.engine
        inspector = inspect(engine)
        
        # Get all existing tables
        existing_tables = inspector.get_table_names()
        
        print("=" * 60)
        print("🔍 DATABASE TABLE CHECK")
        print("=" * 60)
        print(f"\n📊 Connected Database: {engine.url.database}")
        print(f"\n✅ Existing Tables ({len(existing_tables)}):")
        for table in existing_tables:
            print(f"   ✓ {table}")
        
        # Required tables from models
        required_tables = [
            'contacts',
            'careers', 
            'jobs',
            'blogs',
            'testimonials',
            'services',
            'admin_users',
            'comments',
            'analytics'
        ]
        
        print(f"\n📋 Required Tables ({len(required_tables)}):")
        missing_tables = []
        for table in required_tables:
            status = "✓" if table in existing_tables else "✗"
            print(f"   {status} {table}")
            if table not in existing_tables:
                missing_tables.append(table)
        
        print("\n" + "=" * 60)
        
        if missing_tables:
            print(f"\n⚠️  Missing Tables: {', '.join(missing_tables)}")
            print("\n🔧 Creating missing tables...")
            try:
                db.create_all()
                print("\n✅ All tables created successfully!")
                
                # Verify
                inspector = inspect(engine)
                new_tables = inspector.get_table_names()
                print(f"\n📊 Total tables now: {len(new_tables)}")
                for table in new_tables:
                    print(f"   ✓ {table}")
            except Exception as e:
                print(f"\n❌ Error creating tables: {e}")
        else:
            print("\n✅ All required tables already exist!")
        
        print("\n" + "=" * 60)

if __name__ == '__main__':
    check_and_create_tables()
