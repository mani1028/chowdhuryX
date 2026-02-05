"""
Migration Script: Add comment_likes Table
Creates the comment_likes table to track device-based likes for comments

Usage:
    python migrate_add_comment_likes.py
"""
from app import create_app
from models import db, CommentLike
from sqlalchemy import inspect

def migrate_add_comment_likes():
    """Add comment_likes table to database"""
    app = create_app()
    
    with app.app_context():
        inspector = inspect(db.engine)
        existing_tables = inspector.get_table_names()
        
        print("=" * 60)
        print("💬 Comment Likes Table Migration")
        print("=" * 60)
        
        if 'comment_likes' in existing_tables:
            print("⚠️  comment_likes table already exists!")
            print("\nExisting columns:")
            columns = inspector.get_columns('comment_likes')
            for col in columns:
                print(f"  ✓ {col['name']} ({col['type']})")
            return
        
        try:
            print("\n🔨 Creating comment_likes table...")
            
            # Create the table
            CommentLike.__table__.create(db.engine, checkfirst=True)
            
            print("✅ comment_likes table created successfully!")
            print("\nTable structure:")
            print("  ✓ id (INTEGER) - Primary Key")
            print("  ✓ comment_id (INTEGER) - Foreign Key to comments.id")
            print("  ✓ device_id (VARCHAR(255)) - Unique device identifier")
            print("  ✓ ip_address (VARCHAR(45)) - IP address for verification")
            print("  ✓ created_at (DATETIME) - Timestamp")
            print("  ✓ UNIQUE constraint on (comment_id, device_id)")
            
            print("\n" + "=" * 60)
            print("✅ Migration completed successfully!")
            print("=" * 60)
            
        except Exception as e:
            print(f"❌ Error creating table: {str(e)}")
            raise

if __name__ == '__main__':
    migrate_add_comment_likes()
