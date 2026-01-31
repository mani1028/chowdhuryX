# 🚀 ChowdhuryX - Professional Corporate Website

![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-green)
![Database](https://img.shields.io/badge/Database-SQLite%2FPostgreSQL%2FMySQL-blue)

A fully-featured professional corporate website with secure admin panel, blog system with comments, job applications, and comprehensive analytics.

---

## ✨ Key Features

### 🌐 **Public Website**
- Beautiful responsive corporate homepage
- Blog posts with user comments (no login required)
- Service & industry showcase pages
- Job board with applications
- Contact form with admin notifications
- Testimonials system
- Completely mobile-friendly
- SEO optimized (sitemap.xml, robots.txt)

### 👨‍💼 **Admin Panel** (Password Protected)
- 🔐 Secure login with credentials from `.env`
- 📊 Real-time dashboard with statistics
- 💬 Comment moderation (approve/reject/spam)
- 📝 Blog management (create/edit/delete/upload images)
- 📧 Contact & job application management
- 📥 CSV export for data analysis
- 📈 Analytics & engagement tracking
- 🎨 Professional responsive UI

### 🔧 **Technical Stack**
- **Framework:** Flask 2.3+
- **Database:** SQLite/PostgreSQL/MySQL
- **ORM:** SQLAlchemy
- **Authentication:** Session-based with password hashing
- **Security:** CSRF protection, secure cookies, input validation
- **Email:** SMTP support (Gmail, Outlook, custom)
- **Files:** Image upload, resume uploads, CSV export

---

## 🚀 Quick Start

### **Step 1: Setup Environment**
```bash
# Clone/download project
cd chowdhuryx

# Create virtual environment
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 3: Configure Settings**
Edit `.env` file:
```bash
FLASK_ENV=development
ADMIN_USERNAME=admin              # Change this!
ADMIN_PASSWORD=admin123           # Change this!
DATABASE_URL=sqlite:///chowdhuryx.db
```

### **Step 4: Initialize Database & Admin**
```bash
python create_admin.py
```
This creates the database and admin user from `.env` credentials.

### **Step 5: Start App**
```bash
python app.py
```
Open: http://localhost:5000

---

## 🔐 Admin Access

**URL:** http://localhost:5000/admin/login

**Credentials** (from `.env`):
```
Username: admin          (ADMIN_USERNAME)
Password: admin123       (ADMIN_PASSWORD)
```

### **Change Admin Credentials:**

1. **Edit `.env` file:**
   ```
   ADMIN_USERNAME=newadmin
   ADMIN_PASSWORD=NewSecurePass2024!
   ADMIN_EMAIL=newadmin@company.com
   ```

2. **Run setup script:**
   ```bash
   python create_admin.py
   ```

3. **✨ Done!** Database updates automatically with new credentials.

---

## 📋 Environment Configuration (.env)

All settings are managed through `.env` file. No code changes needed!

**Core Settings:**
```bash
# Flask
FLASK_ENV=development              # development or production
FLASK_DEBUG=True                  # Enable debug mode
SECRET_KEY=change-in-production   # Session encryption (CHANGE IN PRODUCTION!)

# Database (auto-created when app starts)
DATABASE_URL=sqlite:///chowdhuryx.db

# Admin Credentials
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
ADMIN_EMAIL=admin@chowdhuryx.com

# Email Setup (for notifications)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-16-char-app-password

# Notifications
ADMIN_EMAILS=admin@chowdhuryx.com
NOTIFY_ON_CONTACT=true
NOTIFY_ON_APPLICATION=true
```

**→ Full Configuration Guide:** [ENVIRONMENT_CONFIG.md](ENVIRONMENT_CONFIG.md)

---

## 🌐 Website Routes

### **Public Pages** (No Login)
| Route | Description |
|-------|-------------|
| `/` | Homepage |
| `/blog` | Blog listing |
| `/blog/<slug>` | Blog post + comments |
| `/services` | All services |
| `/services/<slug>` | Service details |
| `/industries` | All industries |
| `/industries/<slug>` | Industry details |
| `/careers` | Job listings |
| `/contact` | Contact form |
| `/about` | About page |
| `/portfolio` | Portfolio |
| `/testimonials` | Testimonials |
| `/faq` | FAQ |
| `/privacy-policy` | Privacy policy |
| `/terms` | Terms of service |

### **Admin Pages** (Login Required)
| Route | Purpose |
|-------|---------|
| `/admin/login` | Admin login page |
| `/admin/` | Dashboard & statistics |
| `/admin/contacts` | View/manage contacts |
| `/admin/careers` | View/manage applications |
| `/admin/blog` | Blog management |
| `/admin/blog/new` | Create blog post |
| `/admin/comments` | Moderate comments |
| `/admin/analytics` | Analytics & reports |
| `/admin/logout` | Logout |

---

## 💬 Blog & Comment System

### **For Website Visitors:**
- ✅ Read published blog posts
- ✅ Comment with name & email (NO login required!)
- ✅ Like & share posts
- Comments await admin approval before showing

### **For Admin:**
- ✅ Create/edit/delete blog posts
- ✅ Upload featured images
- ✅ Moderate comments (approve/reject/mark spam)
- ✅ View analytics (top posts, engagement)

**→ Detailed Guide:** [BLOG_COMMENT_SYSTEM.md](BLOG_COMMENT_SYSTEM.md)

---

## 📊 Admin Panel Features

### **Dashboard**
- Total contacts, applications, blog posts stats
- Recent activity feed
- Pending comments count
- Popular services & positions
- Top blog posts

### **Contact Management**
- View all contact form submissions
- Filter by status
- Export to CSV
- Bulk actions

### **Career Management**
- View job applications
- Filter & search
- Export to CSV
- Track applicant status

### **Blog Management**
- Create/edit/delete posts
- Upload featured images
- Set publish status (draft/published)
- View post statistics

### **Comment Moderation**
- View all comments
- Approve/reject/mark as spam
- Delete unwanted comments
- Filter by status

### **Analytics**
- Most viewed services
- Most applied positions
- Daily contact trends
- Engagement metrics

---

## 🗄️ Database

### **Automatic Setup**
- Database is **created automatically** when you run `python create_admin.py`
- All tables are initialized with proper relationships
- No manual SQL needed!

### **Supported Databases**

**SQLite** (Default - Local File)
```
DATABASE_URL=sqlite:///chowdhuryx.db
```
Perfect for development and small deployments.

**PostgreSQL** (Recommended for Production)
```
DATABASE_URL=postgresql://username:password@localhost:5432/chowdhuryx
```

**MySQL** (Alternative)
```
DATABASE_URL=mysql://username:password@localhost:3306/chowdhuryx
```

### **To Change Database:**
1. Update `DATABASE_URL` in `.env`
2. Run: `python create_admin.py`
3. New database is created automatically! ✨

---

## 📧 Email Configuration

### **Gmail Setup** (Recommended)
1. Enable 2-Factor Authentication on your Gmail account
2. Generate App Password:
   - Visit: https://myaccount.google.com/apppasswords
   - Select "Mail" and "Windows Computer"
   - Copy the 16-character password
3. Update `.env`:
   ```
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-16-char-app-password
   ```
4. Restart app

### **Other Email Providers:**
- **Outlook:** `smtp.outlook.com:587`
- **SendGrid:** `smtp.sendgrid.net:587`
- **Mailgun:** `smtp.mailgun.org:587`
- **Custom Server:** Enter your SMTP details

### **Notification Settings:**
```bash
ADMIN_EMAILS=admin@company.com,owner@company.com
NOTIFY_ON_CONTACT=true        # Email on new contact
NOTIFY_ON_APPLICATION=true    # Email on new application
NOTIFY_ON_COMMENT=false       # Email on new comment
```

---

## 🛡️ Security Features

### **✓ Implemented**
- Password hashing (pbkdf2:sha256) - industry standard
- CSRF protection on all forms
- Session-based authentication
- File upload validation & sanitization
- SQL injection prevention
- Secure HTTP cookies (HttpOnly, SameSite)
- Input validation on all forms
- Error logging

### **🔒 Best Practices**
- **Change SECRET_KEY in production!**
  ```bash
  python -c "import secrets; print(secrets.token_hex(32))"
  ```
- Use strong admin password (12+ characters)
- Use Gmail App Password, not main password
- Keep `.env` out of version control
- Enable HTTPS in production
- Update dependencies regularly
- Enable email notifications for security events

---

## 📁 Project Structure

```
chowdhuryx/
├── admin/                      # Admin panel blueprint
│   ├── routes.py              # Admin route handlers
│   ├── templates/             # Admin HTML templates
│   │   ├── base-admin.html
│   │   ├── admin-dashboard.html
│   │   ├── admin-blog.html
│   │   ├── admin-comments.html
│   │   └── ...
│   └── static/                # Admin CSS & JS
│
├── templates/                 # Public HTML pages
│   ├── index.html
│   ├── blog.html
│   ├── blog-post.html
│   ├── contact.html
│   └── ...
│
├── static/                    # Public assets
│   ├── css/                  # Stylesheets
│   ├── js/                   # JavaScript
│   ├── images/               # Images & logos
│   └── uploads/              # User uploads
│
├── models.py                 # Database models
├── config.py                 # Configuration loader
├── app.py                    # Main Flask application
├── create_admin.py           # Admin initialization script
├── wsgi.py                   # Production WSGI server
├── .env                      # Environment variables
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── robots.txt / sitemap.xml  # SEO files
```

---

## 🚀 Deployment

### **Development** (Local Testing)
```bash
python app.py
# Opens at http://localhost:5000
```

### **Production** (Live Server)

**Option 1: Gunicorn + Nginx**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
```

**Option 2: Production Mode Settings**
```bash
# .env file
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-generated-secret-key
DATABASE_URL=postgresql://...
```

**Option 3: Hosting Platforms**
- Heroku, PythonAnywhere, AWS, DigitalOcean, etc.
- Each has specific deployment guides
- Set environment variables in platform's config

---

## 🧪 Testing

### **Test Admin Login:**
```
1. Go to http://localhost:5000/admin/login
2. Enter ADMIN_USERNAME and ADMIN_PASSWORD from .env
3. Should see dashboard ✓
```

### **Test Blog Comments:**
```
1. Visit http://localhost:5000/blog
2. Click a blog post
3. Scroll to comments section
4. Enter name, email, comment (NO login needed!)
5. Submit
6. Go to /admin/comments to approve
7. Comment appears after approval ✓
```

### **Test Email Notifications:**
```
1. Configure MAIL_* settings in .env
2. Fill contact form
3. Check admin email inbox
4. Should receive notification ✓
```

---

## 🐛 Troubleshooting

**Problem:** "No module named 'flask'"
- **Solution:** Activate virtual environment first
  ```bash
  # Windows: venv\Scripts\activate
  # Mac/Linux: source venv/bin/activate
  ```

**Problem:** Can't login to admin
- **Solution:** Ensure database was created:
  ```bash
  python create_admin.py
  ```
- **Solution:** Check `.env` credentials match what you entered

**Problem:** Emails not sending
- **Solution:** Verify MAIL_USERNAME and MAIL_PASSWORD
- **Solution:** For Gmail, use 16-char App Password (not regular password)
- **Solution:** Check MAIL_SERVER and MAIL_PORT are correct

**Problem:** "SECRET_KEY" error in logs
- **Solution:** Change SECRET_KEY in .env
  ```bash
  python -c "import secrets; print(secrets.token_hex(32))"
  ```

**Problem:** Database locked / permission errors
- **Solution:** Delete `chowdhuryx.db` and run:
  ```bash
  python create_admin.py
  ```

---

## 📚 Documentation Files

| Document | Contents |
|----------|----------|
| [ENVIRONMENT_CONFIG.md](ENVIRONMENT_CONFIG.md) | Complete .env reference with 22 settings |
| [ADMIN_GUIDE.md](ADMIN_GUIDE.md) | Detailed admin panel usage guide |
| [ADMIN_QUICK_START.md](ADMIN_QUICK_START.md) | Quick admin reference |
| [BLOG_COMMENT_SYSTEM.md](BLOG_COMMENT_SYSTEM.md) | Blog & comment system architecture |
| [README.md](README.md) | This file |

---

## 📦 Requirements

- Python 3.8+
- Flask 2.3+
- SQLAlchemy 2.0+
- Python-dotenv (for .env support)

All requirements listed in `requirements.txt` and installed via:
```bash
pip install -r requirements.txt
```

---

## ⚖️ License

MIT License - Free for personal and commercial use.

---

## 🎯 Quick Reference

### **Change Admin Credentials:**
```bash
# 1. Edit .env
ADMIN_USERNAME=newadmin
ADMIN_PASSWORD=newpassword

# 2. Initialize
python create_admin.py

# 3. Login at /admin/login
```

### **Change Database:**
```bash
# 1. Edit .env
DATABASE_URL=postgresql://user:pass@host/db

# 2. Initialize
python create_admin.py
```

### **Enable Email Notifications:**
```bash
# 1. Edit .env with MAIL_* settings
# 2. Restart app
python app.py
```

### **View Admin Dashboard:**
```
http://localhost:5000/admin/login
(credentials from .env)
```

---

## 🎉 You're Ready!

Your professional corporate website is fully configured and ready to use!

**Next Steps:**
1. ✅ Customize content in templates
2. ✅ Add your company logo & branding
3. ✅ Create blog posts in admin panel
4. ✅ Configure email notifications
5. ✅ Deploy to production

**Need Help?**
- Check documentation files in root directory
- Review error messages in terminal
- Verify `.env` configuration

**Happy Building! 🚀**

