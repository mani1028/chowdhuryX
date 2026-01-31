# Admin Panel - Quick Start Guide

## 🚀 Access Admin Panel

**URL:** `http://localhost:5000/admin/login`

**Login Credentials:**
- Username: `admin`
- Password: `admin123`

⚠️ **Change password immediately after first login!**

---

## 📊 Admin Dashboard Features

Once logged in, you'll have access to:

### **1. Dashboard (`/admin/`)**
- Real-time statistics (contacts, applications, blog posts, comments)
- Recent activity feed
- Popular services and job positions
- Quick metrics overview

### **2. Contact Management (`/admin/contacts`)**
- View all contact form submissions
- Filter by status (new, read, resolved)
- Update contact status
- Delete submissions
- **Export to CSV** with one click

### **3. Career Applications (`/admin/careers`)**
- View all job applications
- Filter by status (applied, shortlisted, rejected, hired)
- Rate candidates (1-5 stars)
- Add internal notes
- Download resumes
- **Export to CSV** with one click

### **4. Blog Management (`/admin/blog`)**
- Create new blog posts
- Upload featured images
- Edit/publish/draft posts
- Manage categories
- Track views

### **5. Comment Moderation (`/admin/comments`)**
- View all user comments
- Approve/reject/mark as spam
- Delete inappropriate comments
- Filter by status

### **6. Analytics (`/admin/analytics`)**
- Most viewed services (last 30 days)
- Most popular blog posts
- Contact submission trends
- Career application trends

---

## 📤 Export Data

### Export Contacts to CSV
1. Go to `/admin/contacts`
2. Click "Export to CSV" button
3. File downloads as `contacts_YYYYMMDD_HHMMSS.csv`

### Export Career Applications to CSV
1. Go to `/admin/careers`
2. Click "Export to CSV" button
3. File downloads as `careers_YYYYMMDD_HHMMSS.csv`

---

## 🖼️ Blog Image Upload

When creating a new blog post:
1. Fill in title, content, excerpt
2. Click "Choose Featured Image"
3. Select PNG/JPG/WEBP file (max 16MB)
4. Image auto-uploads to `static/uploads/blog/`

---

## 🔐 Security

- ✅ Passwords are hashed with `pbkdf2:sha256`
- ✅ Session-based authentication
- ✅ CSRF protection on all forms
- ✅ HttpOnly cookies (prevent XSS)
- ✅ Role-based access control

---

## ⚙️ Admin User Management

### Create Additional Admin Users (Super Admin Only)

**Python Shell:**
```python
python
>>> from app import create_app
>>> from models import db, AdminUser
>>> app = create_app()
>>> with app.app_context():
...     new_admin = AdminUser(
...         username='john',
...         email='john@chowdhuryx.com',
...         full_name='John Doe',
...         role='admin'
...     )
...     new_admin.set_password('SecurePassword123!')
...     db.session.add(new_admin)
...     db.session.commit()
...     print("User created!")
```

---

## 🐛 Troubleshooting

**Admin panel not loading?**
- Ensure Flask server is running: `python app.py`
- Check URL: `http://localhost:5000/admin/login`
- Try clearing browser cache

**Database errors?**
- Reset database: `python create_admin.py`
- Recreates tables and default admin user

**Email notifications not working?**
- Install Flask-Mail: `pip install Flask-Mail`
- Configure `.env` with email settings
- See ADMIN_GUIDE.md for details

---

## 📝 Next Steps

1. ✅ Log in to admin panel
2. ✅ Change admin password
3. ✅ Create additional admin users if needed
4. ✅ Configure email notifications (optional)
5. ✅ Test blog post creation with image upload
6. ✅ Test comment moderation
7. ✅ Review analytics dashboard

---

## 📖 Full Documentation

See [ADMIN_GUIDE.md](ADMIN_GUIDE.md) for comprehensive documentation including:
- Complete feature documentation
- How each system works
- Setup instructions
- Production deployment checklist
- Email configuration
- Comment system integration

---

**Server Status:** ✅ Running at `http://127.0.0.1:5000`
