# ChowdhuryX Admin Panel Guide

## 📋 Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Authentication System](#authentication-system)
4. [Dashboard](#dashboard)
5. [Contact Management](#contact-management)
6. [Career Applications](#career-applications)
7. [Blog Management](#blog-management)
8. [Comment Moderation](#comment-moderation)
9. [Analytics](#analytics)
10. [Data Export](#data-export)
11. [Setup Instructions](#setup-instructions)
12. [How It Works](#how-it-works)
13. [Security Features](#security-features)

---

## 🎯 Overview

The ChowdhuryX Admin Panel is a comprehensive backend management system built with Flask that allows administrators to:
- Manage contact form submissions
- Review and process career applications
- Create, edit, and publish blog posts
- Moderate user comments
- View analytics and insights
- Export data to CSV
- Manage admin users

**Access URL:** `http://localhost:5000/admin/` or `https://chowdhuryx.com/admin/`

---

## ✨ Features

### 🔐 **Secure Authentication**
- Database-driven admin user system
- Password hashing with `werkzeug.security`
- Session-based authentication
- Role-based access control (admin, super_admin)
- Environment variable credentials

### 📊 **Dashboard**
- Real-time statistics (contacts, applications, blog posts, comments)
- Recent activity feed (contacts, applications, comments)
- Analytics charts (popular services, job positions)
- Quick access to all sections

### 📧 **Contact Management**
- View all contact submissions with pagination
- Filter by status (new, read, resolved)
- Update contact status
- Delete unwanted submissions
- **CSV Export** with one click

### 💼 **Career Applications**
- Review all job applications
- Filter by status (applied, shortlisted, rejected, hired)
- Rate candidates (1-5 stars)
- Add internal notes
- **CSV Export** for all applications

### 📝 **Blog Management**
- Create/edit/delete blog posts
- Rich text content editor
- **Image upload** for featured images
- Draft/published status control
- Category management
- SEO-friendly slug generation
- Track views and engagement

### 💬 **Comment Moderation**
- View all user comments on blog posts
- Approve/reject/mark as spam
- Nested comment replies support
- Filter by status (pending, approved, spam, rejected)
- Delete inappropriate comments

### 📈 **Analytics Dashboard**
- Most viewed services (last 30 days)
- Most viewed blog posts
- Contact submission trends
- Career application trends
- Position popularity tracking

### 📤 **Data Export**
- **Contacts to CSV:** Export all contact submissions with full details
- **Careers to CSV:** Export all applications with ratings and status
- Timestamped filenames for easy organization

### 📧 **Email Notifications** (Configurable)
- Alert on new contact submissions
- Alert on new job applications
- Configurable via environment variables

---

## 🔐 Authentication System

### **First-Time Setup: Create Admin User**

Since the system now uses database authentication, you need to create an admin user:

**Option 1: Python Shell**
```python
python
>>> from app import create_app
>>> from models import db, AdminUser
>>> app = create_app()
>>> with app.app_context():
...     admin = AdminUser(username='admin', email='admin@chowdhuryx.com', full_name='Admin User', role='super_admin')
...     admin.set_password('YourSecurePassword123!')
...     db.session.add(admin)
...     db.session.commit()
...     print("Admin user created successfully!")
```

**Option 2: Flask Shell**
```bash
flask shell
>>> from models import db, AdminUser
>>> admin = AdminUser(username='admin', email='admin@chowdhuryx.com', full_name='Admin User', role='super_admin')
>>> admin.set_password('YourSecurePassword123!')
>>> db.session.add(admin)
>>> db.session.commit()
>>> print("Admin user created!")
```

**Option 3: Create via Script**
Create a file `create_admin.py`:
```python
from app import create_app
from models import db, AdminUser

app = create_app()

with app.app_context():
    # Check if admin exists
    if not AdminUser.query.filter_by(username='admin').first():
        admin = AdminUser(
            username='admin',
            email='admin@chowdhuryx.com',
            full_name='System Administrator',
            role='super_admin'
        )
        admin.set_password('ChangeMe123!')
        db.session.add(admin)
        db.session.commit()
        print("✓ Admin user created: username='admin', password='ChangeMe123!'")
        print("⚠️  CHANGE PASSWORD IMMEDIATELY AFTER FIRST LOGIN!")
    else:
        print("Admin user already exists")
```

Run it:
```bash
python create_admin.py
```

### **Login Credentials**
- **URL:** `/admin/login`
- **Default Username:** `admin`
- **Default Password:** (set during admin creation)

⚠️ **IMPORTANT:** Change default password immediately after first login!

---

## 📊 Dashboard

**Access:** `/admin/` or `/admin/dashboard`

### **Statistics Overview**
- **Contacts:** Total and new (unread) count
- **Applications:** Total and pending count
- **Blog Posts:** Total and drafts count
- **Testimonials:** Total and pending count
- **Comments:** Total and pending moderation count

### **Recent Activity**
- Last 5 contact submissions
- Last 5 career applications
- Last 5 pending comments

### **Analytics Insights**
- **Popular Services:** Top 5 most viewed services (last 30 days)
- **Popular Positions:** Top 5 most applied job positions

---

## 📧 Contact Management

**Access:** `/admin/contacts`

### **Features:**
1. **View All Submissions**
   - Paginated list (15 per page)
   - Shows: Name, Email, Subject, Status, Date

2. **Filter by Status**
   - `new` - Unread submissions
   - `read` - Viewed submissions
   - `resolved` - Processed/closed

3. **Actions:**
   - **Update Status:** Click status dropdown to change
   - **Delete:** Remove unwanted/spam submissions
   - **Export CSV:** Download all contacts with one click

### **CSV Export Format:**
```
ID, Name, Email, Phone, Subject, Message, Status, Created At
```

**Export URL:** `/admin/contacts/export`

---

## 💼 Career Applications

**Access:** `/admin/careers`

### **Features:**
1. **View All Applications**
   - Paginated list (15 per page)
   - Shows: Name, Position, Experience, Status, Rating, Date

2. **Filter by Status**
   - `applied` - New applications
   - `shortlisted` - Candidates for interview
   - `rejected` - Not selected
   - `hired` - Successfully hired

3. **Candidate Review:**
   - **Rating:** 1-5 star system
   - **Notes:** Internal comments about candidate
   - **Resume Download:** Access uploaded resumes

4. **Actions:**
   - **Update Status:** Move through hiring pipeline
   - **Rate Candidate:** Assign star rating
   - **Add Notes:** Track interview feedback
   - **Delete:** Remove applications
   - **Export CSV:** Download all applications

### **CSV Export Format:**
```
ID, Full Name, Email, Phone, Position, Experience (Years), Status, Rating, Created At
```

**Export URL:** `/admin/careers/export`

---

## 📝 Blog Management

**Access:** `/admin/blog`

### **Features:**

#### **1. Create New Blog Post**
**URL:** `/admin/blog/new`

**Fields:**
- **Title:** Post headline (auto-generates SEO slug)
- **Content:** Full blog content (rich text)
- **Excerpt:** Short summary for listings
- **Category:** news, technology, case-study, tutorial, etc.
- **Author:** Author name (defaults to logged-in admin)
- **Featured Image:** Upload banner image (JPG, PNG, WEBP)
- **Status:** draft or published

**Image Upload:**
- Supported formats: PNG, JPG, JPEG, GIF, WEBP
- Max size: 16MB
- Auto-naming: `YYYYMMDD_HHMMSS_originalname.ext`
- Storage: `static/uploads/blog/`

#### **2. Edit Existing Post**
**URL:** `/admin/blog/<id>`

- Update content, title, excerpt, category
- Change status (draft ↔ published)
- View all comments on the post
- Track post views

#### **3. Publish/Unpublish**
- **Draft → Published:** Sets `published_at` timestamp
- **Published → Draft:** Hides from public blog

#### **4. Delete Post**
- Permanently removes blog post
- Also deletes associated comments (CASCADE)

### **Blog Post Lifecycle:**
```
Create (Draft) → Edit → Publish → Public View → Analytics
       ↓                                ↓
    Delete ←───────────────────────── Unpublish
```

---

## 💬 Comment Moderation

**Access:** `/admin/comments`

### **Features:**

#### **1. View All Comments**
- Paginated list (20 per page)
- Shows: Author, Blog Post, Content, Status, Date

#### **2. Filter by Status**
- `pending` - Awaiting moderation
- `approved` - Visible on blog
- `spam` - Marked as spam
- `rejected` - Hidden but not deleted

#### **3. Comment Actions:**
- **Approve:** Make visible on blog post
- **Reject:** Hide from public
- **Mark as Spam:** Flag spam comments
- **Delete:** Permanently remove

#### **4. Nested Replies:**
- Comments can have parent-child relationships
- Replies are shown under original comment
- Deleting parent deletes all replies (CASCADE)

### **Comment Workflow:**
```
User submits comment → Status: pending
       ↓
Admin reviews in /admin/comments
       ↓
    ┌──────┬──────┬────────┐
Approve  Reject  Spam   Delete
    ↓       ↓      ↓        ↓
 Visible  Hidden  Hidden  Removed
```

### **How It Works:**
1. Users post comments on blog posts via frontend form
2. Comments are created with `status='pending'`
3. Admin sees pending count on dashboard
4. Admin reviews at `/admin/comments`
5. Admin approves/rejects/marks spam
6. Only approved comments show on public blog

---

## 📈 Analytics

**Access:** `/admin/analytics`

### **Tracked Events:**

#### **1. Service Views**
- Tracks when users view service detail pages
- Shows top 5 most viewed services
- Filterable by time period (7, 30, 90 days)

#### **2. Blog Views**
- Tracks blog post page views
- Top 10 most popular articles
- Engagement metrics

#### **3. Contact Trends**
- Daily contact submission count
- Graph showing submission patterns
- Identify peak inquiry times

#### **4. Career Trends**
- Daily application count
- Most popular job positions
- Hiring funnel metrics

### **How Analytics Work:**

**Data Collection:**
```python
from models import Analytics

# Track service view (add to app.py service_detail route)
analytics = Analytics(
    event_type='service_view',
    event_data='ai-solutions',  # service slug
    ip_address=request.remote_addr,
    user_agent=request.headers.get('User-Agent')
)
db.session.add(analytics)
db.session.commit()
```

**Add to Routes:**
```python
# In app.py - service detail route
@app.route('/services/<slug>')
def service_detail(slug):
    # ... existing code ...
    
    # Track analytics
    from models import Analytics
    analytics = Analytics(
        event_type='service_view',
        event_data=slug,
        ip_address=request.remote_addr,
        user_agent=request.headers.get('User-Agent', '')[:255]
    )
    db.session.add(analytics)
    db.session.commit()
    
    return render_template('service-detail.html', ...)
```

---

## 📤 Data Export

### **Export Contacts to CSV**
**URL:** `/admin/contacts/export`

**Contains:**
- Contact ID
- Name, Email, Phone
- Subject and Message
- Status
- Submission Date

**Filename:** `contacts_YYYYMMDD_HHMMSS.csv`

### **Export Career Applications to CSV**
**URL:** `/admin/careers/export`

**Contains:**
- Application ID
- Full Name, Email, Phone
- Position Applied
- Years of Experience
- Status and Rating
- Application Date

**Filename:** `careers_YYYYMMDD_HHMMSS.csv`

### **Usage:**
1. Navigate to `/admin/contacts` or `/admin/careers`
2. Click "Export to CSV" button
3. File downloads automatically
4. Open in Excel, Google Sheets, or any CSV reader

---

## 🛠️ Setup Instructions

### **1. Environment Variables**

Create `.env` file in project root:

```bash
# Flask Configuration
SECRET_KEY=your-super-secret-key-change-this
FLASK_ENV=development  # or production

# Database (Optional - defaults to SQLite)
DATABASE_URL=sqlite:///chowdhuryX.db

# Email Notifications (Optional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=noreply@chowdhuryx.com

# Admin Email Alerts
ADMIN_EMAILS=admin@chowdhuryx.com,manager@chowdhuryx.com
NOTIFY_ON_CONTACT=true
NOTIFY_ON_APPLICATION=true
```

### **2. Install Dependencies**

```bash
pip install Flask Flask-SQLAlchemy Flask-WTF Flask-Mail werkzeug
```

Or use requirements.txt:
```bash
pip install -r requirements.txt
```

### **3. Initialize Database**

```bash
python
>>> from app import create_app
>>> from models import db
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()
...     print("Database tables created!")
```

### **4. Create Admin User**

See [Authentication System](#authentication-system) section above.

### **5. Create Upload Directories**

```bash
# Windows PowerShell
New-Item -ItemType Directory -Force -Path "static/uploads/blog"
New-Item -ItemType Directory -Force -Path "static/uploads/resumes"

# Linux/Mac
mkdir -p static/uploads/blog
mkdir -p static/uploads/resumes
```

### **6. Run Application**

```bash
python app.py
# OR
flask run
```

**Access Admin:** `http://localhost:5000/admin/login`

---

## 🔧 How It Works

### **Architecture Overview**

```
┌─────────────────────────────────────────────┐
│          Frontend (Public Site)             │
│  /services /blog /contact /careers          │
└────────────┬────────────────────────────────┘
             │
             ├─ Contact Form → Contact Model → Admin Panel
             ├─ Career Form → Career Model → Admin Panel
             ├─ Blog Posts → Blog Model → Admin Management
             └─ Comments → Comment Model → Admin Moderation
                           ↓
┌─────────────────────────────────────────────┐
│           Admin Panel (/admin/*)            │
│  Authentication → Session → Role Check      │
└────────────┬────────────────────────────────┘
             │
    ┌────────┼────────┐
    ↓        ↓        ↓
Dashboard  Management  Tools
  Stats    CRUD Ops   Export/Analytics
```

### **Database Models**

#### **AdminUser**
```python
- id (Primary Key)
- username (Unique)
- email (Unique)
- password_hash (Encrypted)
- role (admin | super_admin)
- is_active (Boolean)
- last_login (Timestamp)
```

#### **Contact**
```python
- id, name, email, phone, subject, message
- status (new | read | resolved)
- created_at, ip_address
```

#### **Career**
```python
- id, full_name, email, phone, position
- experience_years, resume_filename, cover_letter
- status (applied | shortlisted | rejected | hired)
- rating (1-5 stars)
- notes (admin comments)
```

#### **Blog**
```python
- id, title, slug, author, category
- content, excerpt, featured_image
- status (draft | published | archived)
- views, created_at, updated_at, published_at
```

#### **Comment**
```python
- id, blog_id, author_name, author_email, content
- status (pending | approved | spam | rejected)
- parent_id (for nested replies)
- created_at, ip_address
```

#### **Analytics**
```python
- id, event_type, event_data
- ip_address, user_agent, created_at
```

### **Request Flow**

**Example: Contact Form Submission**
```
1. User fills form at /contact
2. POST to /contact route in app.py
3. Validate form data
4. Create Contact model instance
5. Save to database
6. (Optional) Send email notification to admin
7. Track analytics event
8. Redirect with success message
9. Admin sees new contact in /admin/contacts
```

**Example: Blog Comment Moderation**
```
1. User posts comment on blog post
2. Comment created with status='pending'
3. Admin sees pending count on dashboard
4. Admin navigates to /admin/comments
5. Reviews comment content
6. Clicks "Approve" button
7. AJAX POST to /admin/comment/<id>/status
8. Updates status to 'approved'
9. Comment now visible on public blog
```

---

## 🔒 Security Features

### **1. Password Security**
- Passwords hashed using `werkzeug.security`
- `pbkdf2:sha256` algorithm with salt
- Never store plain text passwords

### **2. Session Security**
- Session-based authentication
- HttpOnly cookies (prevent XSS)
- SameSite=Lax (CSRF protection)
- Configurable session lifetime (7 days default)

### **3. CSRF Protection**
- Flask-WTF CSRF tokens on all forms
- Required for POST/PUT/DELETE requests

### **4. File Upload Security**
- Whitelist allowed extensions
- `secure_filename()` sanitization
- File size limits (16MB default)
- Timestamp-based unique naming

### **5. SQL Injection Prevention**
- SQLAlchemy ORM (parameterized queries)
- No raw SQL concatenation

### **6. Role-Based Access**
- `@login_required` decorator on all admin routes
- Super admin role for user management
- Regular admin for content management

### **7. Environment Variables**
- Sensitive config in `.env` (not in Git)
- Production uses strong `SECRET_KEY`
- Database credentials externalized

---

## 🚀 Production Deployment Checklist

- [ ] Change default admin password
- [ ] Set strong `SECRET_KEY` in environment
- [ ] Configure production database (PostgreSQL/MySQL)
- [ ] Set up email server (Gmail, SendGrid, AWS SES)
- [ ] Enable HTTPS (SSL certificate)
- [ ] Set `SESSION_COOKIE_SECURE=True`
- [ ] Configure firewall rules
- [ ] Set up database backups
- [ ] Test CSV export functionality
- [ ] Test email notifications
- [ ] Review analytics tracking
- [ ] Set up monitoring/logging

---

## 📞 Support

For issues or questions:
- **Email:** support@chowdhuryx.com
- **Documentation:** Check README.md
- **Database Issues:** Run `db.create_all()` to recreate tables

---

## 📝 License

© 2026 ChowdhuryX. All rights reserved.
