"""
Database Migration Script
Adds new columns to existing database without losing data
"""

import sqlite3
import os

def migrate_database():
    # Get database path
    db_path = os.getenv('DATABASE_URL', 'sqlite:///instance/chowdhuryX.db')
    db_path = db_path.replace('sqlite:///', '')
    
    # Make it absolute path
    if not os.path.isabs(db_path):
        db_path = os.path.join(os.path.dirname(__file__), db_path)
    
    if not os.path.exists(db_path):
        print(f"❌ Database not found at: {db_path}")
        return False
    
    print(f"📂 Database: {db_path}")
    print("=" * 60)
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    migrations_run = 0
    migrations_skipped = 0
    
    # Migration 1: Add image_url to blog table
    try:
        cursor.execute("ALTER TABLE blog ADD COLUMN image_url VARCHAR(500)")
        conn.commit()
        print("✅ Added 'image_url' column to blog table")
        migrations_run += 1
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e).lower():
            print("ℹ️  'image_url' column already exists in blog table")
            migrations_skipped += 1
        else:
            print(f"❌ Error adding image_url: {e}")
    
    # Migration 2: Add excerpt to blog table
    try:
        cursor.execute("ALTER TABLE blog ADD COLUMN excerpt TEXT")
        conn.commit()
        print("✅ Added 'excerpt' column to blog table")
        migrations_run += 1
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e).lower():
            print("ℹ️  'excerpt' column already exists in blog table")
            migrations_skipped += 1
        else:
            print(f"❌ Error adding excerpt: {e}")
    
    # Verify the changes
    print("\n" + "=" * 60)
    print("📋 Verifying blog table structure:")
    cursor.execute("PRAGMA table_info(blog)")
    columns = cursor.fetchall()
    for col in columns:
        print(f"   - {col[1]} ({col[2]})")
    
    conn.close()
    
    print("\n" + "=" * 60)
    print(f"✅ Migrations completed: {migrations_run}")
    print(f"ℹ️  Migrations skipped: {migrations_skipped}")
    print("=" * 60)
    
    return True

if __name__ == '__main__':
    print("\n🔧 ChowdhuryX Database Migration Tool")
    print("=" * 60)
    
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    # Run migration
    success = migrate_database()
    
    if success:
        print("\n✅ Migration completed successfully!")
        print("\nYou can now use the new fields in your application:")
        print("  - blog.image_url (for banner images)")
        print("  - blog.excerpt (for preview text)")
    else:
        print("\n❌ Migration failed. Please check the errors above.")
