# 🔧 Environment Configuration Guide (.env)

## Overview

The `.env` file contains all configuration settings for your ChowdhuryX application. Instead of hardcoding values in Python files, we use environment variables that can be easily changed without touching code.

**Key Benefit:** Change admin credentials, database, email settings, etc., without rewriting code!

---

## 📋 Complete .env Settings Reference

### **1️⃣ FLASK_ENV**
```
FLASK_ENV=development
```
**Values:** `development` or `production`
- `development`: Debug mode ON, auto-reload on file changes, detailed error messages
- `production`: Debug mode OFF, optimized performance, minimal error details

**Usage:** Controls Flask's behavior. Use `development` during development, `production` for live sites.

---

### **2️⃣ FLASK_DEBUG**
```
FLASK_DEBUG=True
```
**Values:** `True` or `False`
- `True`: Shows detailed error pages, auto-reloads app when code changes
- `False`: Clean error pages, no auto-reload

**Usage:** Keep `True` during development, set to `False` in production.

---

### **3️⃣ SECRET_KEY**
```
SECRET_KEY=dev-secret-key-change-in-production
```
**Purpose:** Encrypts session data and CSRF tokens

**⚠️ CRITICAL:** 
- Must be changed in production!
- Generate strong key: 
  ```bash
  python -c "import secrets; print(secrets.token_hex(32))"
  ```
- Example production value: `a7f9d8e2c1b4f6a9e8c7d5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5`

---

### **4️⃣ DATABASE_URL**
```
DATABASE_URL=sqlite:///chowdhuryX.db
```
**Supported Options:**

| Database | Connection String | When to Use |
|----------|------------------|------------|
| SQLite (Local File) | `sqlite:///chowdhuryX.db` | Development, small projects |
| PostgreSQL | `postgresql://user:pass@localhost/dbname` | Production, larger projects |
| MySQL | `mysql://user:pass@localhost/dbname` | Production, hosted servers |

**Examples:**
```bash
# Local SQLite (default)
DATABASE_URL=sqlite:///chowdhuryX.db

# PostgreSQL (production)
DATABASE_URL=postgresql://admin:mypassword@db.example.com:5432/chowdhuryx

# MySQL (hosting providers)
DATABASE_URL=mysql://root:password@localhost/chowdhuryx
```

**Note:** Database is automatically created when app starts!

---

### **5️⃣ ADMIN_USERNAME**
```
ADMIN_USERNAME=admin
```
**Purpose:** Username to login to admin panel at `/admin/login`

**Examples:**
- `admin` (default)
- `john_doe`
- `chowdhuryx_admin`

**To Change:**
1. Edit `.env`: `ADMIN_USERNAME=newusername`
2. Run: `python create_admin.py`
3. Database updates automatically! ✨

---

### **6️⃣ ADMIN_PASSWORD**
```
ADMIN_PASSWORD=admin123
```
**Purpose:** Password to login to admin panel

**⚠️ SECURITY:**
- Use strong password in production!
- Minimum 12 characters recommended
- Include uppercase, lowercase, numbers, special characters

**Examples:**
- Development: `admin123` ✓
- Production: `Ch0wdh@ry2024Secure!` ✓

**To Change:**
1. Edit `.env`: `ADMIN_PASSWORD=newsecurepassword`
2. Run: `python create_admin.py`
3. Password is automatically hashed in database
4. Database updates automatically! ✨

---

### **7️⃣ ADMIN_EMAIL**
```
ADMIN_EMAIL=admin@chowdhuryx.com
```
**Purpose:** Admin email address for notifications and display

**Used For:**
- Display name in admin panel
- Receiving notifications (when enabled)
- Billing/important updates

---

### **8️⃣ MAIL_SERVER**
```
MAIL_SERVER=smtp.gmail.com
```
**Popular SMTP Servers:**

| Email Provider | SMTP Server | Port | TLS |
|---|---|---|---|
| Gmail | `smtp.gmail.com` | 587 | True |
| Gmail (SSL) | `smtp.gmail.com` | 465 | False |
| Outlook | `smtp.outlook.com` | 587 | True |
| SendGrid | `smtp.sendgrid.net` | 587 | True |
| Mailgun | `smtp.mailgun.org` | 587 | True |

---

### **9️⃣ MAIL_PORT**
```
MAIL_PORT=587
```
**Common Ports:**
- `587` - TLS (Transport Layer Security) - Most common
- `465` - SSL (Secure Sockets Layer) - Alternative
- `25` - Unencrypted (not recommended)

---

### **🔟 MAIL_USE_TLS**
```
MAIL_USE_TLS=True
```
**Values:** `True` or `False`
- `True`: Use TLS encryption (port 587)
- `False`: Don't use TLS (port 465 or 25)

**For Gmail:** Always use `True` with port 587

---

### **1️⃣1️⃣ MAIL_USERNAME**
```
MAIL_USERNAME=your-email@gmail.com
```
**Purpose:** Email address to send emails from

**For Gmail:**
1. Enable 2-Factor Authentication
2. Go to: https://myaccount.google.com/apppasswords
3. Generate App Password (16 characters)
4. Use email address here

---

### **1️⃣2️⃣ MAIL_PASSWORD**
```
MAIL_PASSWORD=your-app-password
```
**⚠️ CRITICAL:** 
- For Gmail: Use App Password, NOT your regular password!
- Set up at: https://myaccount.google.com/apppasswords
- Example: `abcd efgh ijkl mnop` (16 characters)

**Never use your main Gmail password!**

---

### **1️⃣3️⃣ MAIL_DEFAULT_SENDER**
```
MAIL_DEFAULT_SENDER=noreply@chowdhuryX.com
```
**Format:** `"Company Name <email@example.com>"`

**Used For:** Default sender address in email notifications

---

### **1️⃣4️⃣ ADMIN_EMAILS**
```
ADMIN_EMAILS=admin@chowdhuryx.com
```
**Multiple Emails:** Comma-separated
```
ADMIN_EMAILS=admin@chowdhuryx.com,owner@chowdhuryx.com,manager@chowdhuryx.com
```

**Receives Notifications For:**
- New contact form submissions
- New job applications
- New blog comments (when enabled)

---

### **1️⃣5️⃣ NOTIFY_ON_CONTACT**
```
NOTIFY_ON_CONTACT=true
```
**Values:** `true` or `false`
- `true`: Send email when someone submits contact form
- `false`: Don't send notifications

---

### **1️⃣6️⃣ NOTIFY_ON_APPLICATION**
```
NOTIFY_ON_APPLICATION=true
```
**Values:** `true` or `false`
- `true`: Send email when someone applies for a job
- `false`: Don't send notifications

---

### **1️⃣7️⃣ NOTIFY_ON_COMMENT**
```
NOTIFY_ON_COMMENT=false
```
**Values:** `true` or `false`
- `true`: Send email when someone posts a blog comment
- `false`: Don't send notifications

---

### **1️⃣8️⃣ MAX_FILE_SIZE**
```
MAX_FILE_SIZE=16
```
**Unit:** MB (Megabytes)
- `16` = 16 MB max upload size
- Used for resumes, images, documents

---

### **1️⃣9️⃣ ALLOWED_EXTENSIONS**
```
ALLOWED_EXTENSIONS=pdf,doc,docx,png,jpg,jpeg,gif
```
**Allowed File Types:** Comma-separated

**For Resume Uploads:**
```
ALLOWED_EXTENSIONS=pdf,doc,docx
```

**For All Files:**
```
ALLOWED_EXTENSIONS=pdf,doc,docx,xls,xlsx,png,jpg,jpeg,gif,zip
```

---

### **2️⃣0️⃣ ALLOWED_IMAGE_EXTENSIONS**
```
ALLOWED_IMAGE_EXTENSIONS=png,jpg,jpeg,gif,webp
```
**Used For:** Blog post featured images

---

### **2️⃣1️⃣ SESSION_TIMEOUT**
```
SESSION_TIMEOUT=7
```
**Unit:** Days
- `7` = Session lasts 7 days
- After timeout, user must login again

---

### **2️⃣2️⃣ ITEMS_PER_PAGE**
```
ITEMS_PER_PAGE=10
```
**Used For:** Pagination in:
- Blog posts list
- Contact submissions
- Job applications
- Comments

---

## 🚀 Common Scenarios

### **Scenario 1: Change Admin Credentials**

**Current:**
```
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
ADMIN_EMAIL=admin@chowdhuryx.com
```

**Want to change to:**
```
ADMIN_USERNAME=john_admin
ADMIN_PASSWORD=SecurePass2024!
ADMIN_EMAIL=john@chowdhuryx.com
```

**Steps:**
1. Edit `.env` with new values ✏️
2. Run: `python create_admin.py` 🔄
3. Database updated automatically! ✨
4. Login with new credentials at `/admin/login` 🔐

---

### **Scenario 2: Use PostgreSQL for Production**

**Current:**
```
DATABASE_URL=sqlite:///chowdhuryX.db
```

**Change to PostgreSQL:**
```
DATABASE_URL=postgresql://postgres:mypassword@db.example.com:5432/chowdhuryx
```

**Steps:**
1. Create database on PostgreSQL server
2. Update `.env` with connection string
3. Run: `python create_admin.py` (rebuilds database)
4. Start app: `python app.py`

---

### **Scenario 3: Enable Email Notifications**

**Setup Gmail:**
```
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=company@gmail.com
MAIL_PASSWORD=xyzw abcd efgh ijkl  (16-char App Password)
NOTIFY_ON_CONTACT=true
NOTIFY_ON_APPLICATION=true
```

**Steps:**
1. Generate App Password: https://myaccount.google.com/apppasswords
2. Update `.env` with credentials
3. Restart app
4. Test by submitting contact form

---

### **Scenario 4: Production Deployment**

```
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=a7f9d8e2c1b4f6a9e8c7d5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5
DATABASE_URL=postgresql://user:pass@production-db.com/chowdhuryx
ADMIN_USERNAME=admin_prod
ADMIN_PASSWORD=VerySecure@2024!
MAIL_USERNAME=noreply@company.com
MAIL_PASSWORD=smtp-app-password-here
```

---

## 📝 How to Edit .env

### **Option 1: Edit File Directly** (Easiest)
```
1. Open .env in text editor (VS Code, Notepad, etc.)
2. Change any values
3. Save file
4. Run: python create_admin.py (if you changed admin credentials)
5. Restart Flask app
```

### **Option 2: Command Line**
```bash
# Change ADMIN_PASSWORD
# Linux/Mac:
sed -i 's/ADMIN_PASSWORD=.*/ADMIN_PASSWORD=newpassword/' .env

# Windows PowerShell:
(Get-Content .env) -replace 'ADMIN_PASSWORD=.*', 'ADMIN_PASSWORD=newpassword' | Set-Content .env

# Then update database:
python create_admin.py
```

---

## 🔒 Security Best Practices

### ✅ DO:
- Change `SECRET_KEY` in production
- Use strong `ADMIN_PASSWORD` (12+ characters)
- Use Gmail App Password, not main password
- Enable `NOTIFY_*` options for security events
- Keep `.env` out of version control (add to `.gitignore`)

### ❌ DON'T:
- Commit `.env` to GitHub
- Use same password for admin and email
- Hardcode secrets in Python files
- Use weak passwords in production
- Share `.env` file publicly

---

## 🧪 Test Your Configuration

### **Test Database Connection:**
```bash
python -c "from app import create_app; app = create_app(); print('✓ Database OK')"
```

### **Test Email Settings:**
```bash
python -c "
from app import create_app
from models import AdminUser
app = create_app()
print('✓ Email config loaded')
print(f'  SMTP: {app.config[\"MAIL_SERVER\"]}:{app.config[\"MAIL_PORT\"]}')
"
```

### **Test Admin Login:**
1. Run `python app.py`
2. Go to `http://localhost:5000/admin/login`
3. Enter `ADMIN_USERNAME` and `ADMIN_PASSWORD` from `.env`
4. Should see dashboard ✨

---

## 📞 Troubleshooting

**Problem:** Can't login to admin panel
- **Solution:** Check `ADMIN_USERNAME` and `ADMIN_PASSWORD` in `.env`
- **Solution:** Run `python create_admin.py` to update database

**Problem:** Emails not sending
- **Solution:** Verify `MAIL_USERNAME` and `MAIL_PASSWORD`
- **Solution:** Check `MAIL_SERVER` and `MAIL_PORT`
- **Solution:** For Gmail, use App Password, not regular password

**Problem:** Database connection error
- **Solution:** Verify `DATABASE_URL` syntax
- **Solution:** For PostgreSQL, ensure database exists
- **Solution:** Check username/password in connection string

**Problem:** "SECRET_KEY" error in production
- **Solution:** Generate new key: `python -c "import secrets; print(secrets.token_hex(32))"`
- **Solution:** Update `.env` with generated key
- **Solution:** Restart app

---

## 🎯 Summary

| Task | Edit in | Then Run | Result |
|------|---------|----------|--------|
| Change admin username/password | `.env` | `python create_admin.py` | ✅ Database updated |
| Change email settings | `.env` | Restart app | ✅ Ready to send emails |
| Change database | `.env` | `python create_admin.py` | ✅ New database created |
| Deploy to production | `.env` | `python app.py` | ✅ Production ready |

---

## 📚 Related Files

- **[README.md](README.md)** - Quick start guide
- **[ADMIN_GUIDE.md](ADMIN_GUIDE.md)** - Admin panel usage
- **[config.py](../config.py)** - Python configuration loader
- **[create_admin.py](../create_admin.py)** - Script to initialize admin user

