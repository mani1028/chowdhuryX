# Database Migration Guide

## Overview
This guide helps you update your existing database schema without losing data when you've added new fields to your models.

## Current Situation
You have an existing database with content, and we've added new fields to the models:
- **Blog model**: Added `image_url` and `excerpt` fields
- **Job model**: Already has all necessary fields

## Migration Options

### Option 1: Flask-Migrate (Recommended for Production)

Flask-Migrate uses Alembic to handle database schema changes automatically.

#### 1. Install Flask-Migrate
```bash
pip install Flask-Migrate
```

#### 2. Update requirements.txt
Add this line to your requirements.txt:
```
Flask-Migrate==4.0.5
```

#### 3. Initialize Flask-Migrate in app.py

Add these lines to your `app.py`:

```python
from flask_migrate import Migrate

# After creating the app
migrate = Migrate(app, db)
```

#### 4. Initialize Migration Repository
```bash
# This creates a migrations folder
flask db init
```

#### 5. Create Initial Migration
```bash
# This creates a migration script based on your current models
flask db migrate -m "Add image_url and excerpt to Blog model"
```

#### 6. Review the Migration
Open the generated migration file in `migrations/versions/` and verify the changes:
- Should add `image_url` column to blog table
- Should add `excerpt` column to blog table

#### 7. Apply the Migration
```bash
# This applies the migration to your database
flask db upgrade
```

#### 8. For Future Changes
Whenever you update your models:
```bash
flask db migrate -m "Description of changes"
flask db upgrade
```

---

### Option 2: Manual SQL Migration (SQLite)

If you're still using SQLite and want a quick fix:

#### 1. Create a Python Script

Create `migrate_db.py`:

```python
import sqlite3
import os

# Get the database path from environment or use default
db_path = os.getenv('DATABASE_URL', 'sqlite:///instance/chowdhuryX.db')
db_path = db_path.replace('sqlite:///', '')

# Connect to database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    # Add image_url column to blog table
    cursor.execute("ALTER TABLE blog ADD COLUMN image_url VARCHAR(500)")
    print("✓ Added image_url column to blog table")
except sqlite3.OperationalError as e:
    if "duplicate column name" in str(e):
        print("✓ image_url column already exists")
    else:
        print(f"✗ Error adding image_url: {e}")

try:
    # Add excerpt column to blog table
    cursor.execute("ALTER TABLE blog ADD COLUMN excerpt TEXT")
    print("✓ Added excerpt column to blog table")
except sqlite3.OperationalError as e:
    if "duplicate column name" in str(e):
        print("✓ excerpt column already exists")
    else:
        print(f"✗ Error adding excerpt: {e}")

# Commit changes
conn.commit()
conn.close()

print("\n✓ Database migration completed successfully!")
```

#### 2. Run the Migration Script
```bash
python migrate_db.py
```

---

### Option 3: Manual PostgreSQL Migration

When you move to PostgreSQL on your VPS:

#### 1. Connect to PostgreSQL
```bash
psql -U your_username -d your_database_name
```

#### 2. Run ALTER TABLE Commands
```sql
-- Add image_url column
ALTER TABLE blog ADD COLUMN image_url VARCHAR(500);

-- Add excerpt column
ALTER TABLE blog ADD COLUMN excerpt TEXT;

-- Verify changes
\d blog
```

#### 3. Exit PostgreSQL
```sql
\q
```

---

## Migration Strategy for Moving to Production

### Step 1: Export SQLite Data
```python
# Create export_data.py
from app import create_app, db
from models import Blog, Job, Contact, Career, AdminUser
import json

app = create_app()
with app.app_context():
    # Export blogs
    blogs = Blog.query.all()
    blogs_data = [blog.to_dict() for blog in blogs]
    
    # Export jobs
    jobs = Job.query.all()
    jobs_data = [job.to_dict() for job in jobs]
    
    # Export contacts
    contacts = Contact.query.all()
    contacts_data = [c.to_dict() for c in contacts]
    
    # Export careers (applications)
    careers = Career.query.all()
    careers_data = [c.to_dict() for c in careers]
    
    # Save to JSON files
    with open('export_blogs.json', 'w') as f:
        json.dump(blogs_data, f, indent=2, default=str)
    
    with open('export_jobs.json', 'w') as f:
        json.dump(jobs_data, f, indent=2, default=str)
    
    with open('export_contacts.json', 'w') as f:
        json.dump(contacts_data, f, indent=2, default=str)
    
    with open('export_careers.json', 'w') as f:
        json.dump(careers_data, f, indent=2, default=str)
    
    print("✓ Data exported successfully!")
```

Run it:
```bash
python export_data.py
```

### Step 2: Setup PostgreSQL on VPS

1. Install PostgreSQL:
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

2. Create database and user:
```bash
sudo -u postgres psql

CREATE DATABASE chowdhuryx_db;
CREATE USER chowdhuryx WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE chowdhuryx_db TO chowdhuryx;
\q
```

3. Update .env file on VPS:
```
DATABASE_URL=postgresql://chowdhuryx:your_secure_password@localhost:5432/chowdhuryx_db
```

### Step 3: Create Tables on PostgreSQL
```bash
# On your VPS
flask db upgrade  # If using Flask-Migrate
# OR
python
>>> from app import create_app, db
>>> app = create_app()
>>> with app.app_context():
>>>     db.create_all()
>>> exit()
```

### Step 4: Import Data to PostgreSQL

Create `import_data.py`:
```python
from app import create_app, db
from models import Blog, Job, Contact, Career
import json
from datetime import datetime

app = create_app()

def parse_datetime(dt_str):
    if not dt_str:
        return None
    try:
        return datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
    except:
        return None

with app.app_context():
    # Import blogs
    with open('export_blogs.json', 'r') as f:
        blogs_data = json.load(f)
        for data in blogs_data:
            blog = Blog(
                id=data['id'],
                title=data['title'],
                content=data['content'],
                excerpt=data.get('excerpt'),
                image_url=data.get('image_url'),
                author=data['author'],
                status=data['status'],
                views=data.get('views', 0),
                created_at=parse_datetime(data.get('created_at')),
                updated_at=parse_datetime(data.get('updated_at'))
            )
            db.session.add(blog)
    
    # Import jobs
    with open('export_jobs.json', 'r') as f:
        jobs_data = json.load(f)
        for data in jobs_data:
            job = Job(
                id=data['id'],
                title=data['title'],
                description=data['description'],
                requirements=data.get('requirements'),
                responsibilities=data.get('responsibilities'),
                location=data['location'],
                job_type=data['job_type'],
                department=data.get('department'),
                experience_required=data.get('experience_required'),
                salary_range=data.get('salary_range'),
                status=data['status'],
                views=data.get('views', 0),
                created_at=parse_datetime(data.get('created_at')),
                updated_at=parse_datetime(data.get('updated_at')),
                closes_at=parse_datetime(data.get('closes_at'))
            )
            db.session.add(job)
    
    # Import contacts
    with open('export_contacts.json', 'r') as f:
        contacts_data = json.load(f)
        for data in contacts_data:
            contact = Contact(
                id=data['id'],
                name=data['name'],
                email=data['email'],
                subject=data.get('subject'),
                message=data['message'],
                status=data.get('status', 'new'),
                created_at=parse_datetime(data.get('created_at'))
            )
            db.session.add(contact)
    
    # Import career applications
    with open('export_careers.json', 'r') as f:
        careers_data = json.load(f)
        for data in careers_data:
            career = Career(
                id=data['id'],
                position=data['position'],
                name=data['name'],
                email=data['email'],
                phone=data.get('phone'),
                resume_path=data.get('resume_path'),
                cover_letter=data.get('cover_letter'),
                status=data.get('status', 'new'),
                created_at=parse_datetime(data.get('created_at'))
            )
            db.session.add(career)
    
    # Commit all changes
    db.session.commit()
    print("✓ Data imported successfully!")
```

Run on VPS:
```bash
# Upload JSON files and import_data.py to VPS
python import_data.py
```

---

## Quick Start for Development (SQLite)

If you just want to update your local SQLite database:

1. **Backup your database first:**
```bash
copy instance\chowdhuryX.db instance\chowdhuryX.db.backup
```

2. **Create and run the migration script:**
```bash
python migrate_db.py
```

3. **Verify the changes work:**
```bash
python
>>> from app import create_app, db
>>> from models import Blog
>>> app = create_app()
>>> with app.app_context():
>>>     blog = Blog.query.first()
>>>     print(blog.image_url)  # Should work without errors
>>>     print(blog.excerpt)  # Should work without errors
>>> exit()
```

---

## Recommended Approach

1. **For Local Development (Now):**
   - Use the manual SQL migration script (Option 2)
   - Quick and simple for SQLite

2. **For Production (VPS):**
   - Install Flask-Migrate (Option 1)
   - Proper version control of database changes
   - Easy to rollback if needed

3. **For Moving to Production:**
   - Export data from SQLite
   - Setup PostgreSQL on VPS
   - Import data to PostgreSQL
   - Use Flask-Migrate for future changes

---

## Need Help?

If you encounter any issues:
1. Make sure you have a backup of your database
2. Check the error messages carefully
3. Verify your DATABASE_URL in .env is correct
4. Make sure all required columns have default values or allow NULL

## Common Issues

### "Column already exists"
- The migration was already run
- Safe to ignore this error

### "Table doesn't exist"
- Run `db.create_all()` first
- Or use `flask db upgrade`

### "Cannot add NOT NULL column without default"
- Update the migration to add nullable columns
- Or provide default values in the migration
