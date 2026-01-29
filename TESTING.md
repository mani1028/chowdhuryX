# Testing Instructions for ChowdhuryX Website

## 🚀 Quick Start

### 1. Initial Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration
```bash
# Copy .env example to .env
cp .env.example .env

# Edit .env with your settings (optional for development)
# Default settings are fine for local development
```

### 3. Run the Application
```bash
# Start the Flask development server
python app.py

# The application will start at:
# - Public Site: http://localhost:5000
# - Admin Panel: http://localhost:5000/admin
```

## 📝 Testing the Features

### Public Website
1. **Homepage** - http://localhost:5000
   - Check hero section displays correctly
   - Verify responsive design on mobile/tablet
   - Test navigation menu

2. **About Page** - http://localhost:5000/about
   - View company info and team members
   - Check mission/vision cards

3. **Services** - http://localhost:5000/services
   - Browse service offerings
   - Test responsive layout

4. **Careers** - http://localhost:5000/careers
   - View job listings
   - Click "Apply Now" button
   - Fill and submit job application form

5. **Contact** - http://localhost:5000/contact
   - Fill contact form
   - Verify form validation
   - Submit and check success message

6. **Blog** - http://localhost:5000/blog
   - View blog listing page
   - Click on articles to read full posts

### Admin Panel

#### Access Admin
- URL: http://localhost:5000/admin
- Username: `admin`
- Password: `admin123`

#### Test Admin Features

1. **Dashboard** - http://localhost:5000/admin/dashboard
   - View statistics
   - Check recent activity

2. **Contacts** - http://localhost:5000/admin/contacts
   - View submitted contact forms
   - Filter by status (new, read, resolved)
   - Click to view full contact details
   - Update contact status

3. **Career Applications** - http://localhost:5000/admin/careers
   - View all job applications
   - Filter by status (applied, shortlisted, hired, rejected)
   - Rate applications (1-5 stars)
   - Add notes
   - Download resumes

4. **Blog Management** - http://localhost:5000/admin/blog
   - Create new blog post
   - Edit existing posts
   - Change post status (draft, published, archived)
   - View post analytics

## 🧪 Browser Testing Checklist

### Cross-Browser
- [ ] Chrome/Chromium
- [ ] Firefox
- [ ] Safari
- [ ] Edge

### Responsive Design
- [ ] Desktop (1920x1080)
- [ ] Tablet (768px width)
- [ ] Mobile (375px width)

### Forms
- [ ] Contact form validation
- [ ] Career application form
- [ ] Admin login

### Navigation
- [ ] Header menu links work
- [ ] Footer links work
- [ ] Mobile menu toggle works
- [ ] Pagination works on blog

## 🔍 Database Testing

The application uses SQLite by default. Check the database:

```bash
# Install sqlite3 command line tool (if needed)
# Windows: Use DB Browser for SQLite or similar tool
# Mac: brew install sqlite
# Linux: sudo apt install sqlite3

# View database
sqlite3 chowdhuryX.db

# List tables
.tables

# View contacts
SELECT * FROM contacts;

# View career applications
SELECT * FROM careers;

# View blog posts
SELECT * FROM blogs;
```

## 🐛 Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution**: Make sure virtual environment is activated
```bash
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### Issue: "Port 5000 already in use"
**Solution**: Change the port in app.py or kill the process using it
```bash
# Linux/Mac: Find and kill process
lsof -i :5000
kill -9 <PID>

# Windows: Change port in app.py
app.run(port=5001)
```

### Issue: Database errors
**Solution**: Delete the database file and restart
```bash
# Linux/Mac
rm chowdhuryX.db

# Windows
del chowdhuryX.db

# Restart the application to recreate
python app.py
```

## ✅ Final Checklist

Before going to production:
- [ ] All pages load without errors
- [ ] Forms submit and save to database
- [ ] Admin panel is accessible and functional
- [ ] Responsive design works on mobile
- [ ] No console errors in browser
- [ ] Database operations work correctly
- [ ] Admin authentication works
- [ ] File uploads work (if enabled)
- [ ] Email notifications configured (if enabled)

## 📊 Performance Testing

```bash
# Install Apache Bench (optional)
# Mac: brew install httpd
# Linux: sudo apt install apache2-utils

# Test homepage response time
ab -n 100 -c 10 http://localhost:5000/

# Results will show requests per second, response times, etc.
```

## 📚 Additional Resources

- Flask Documentation: https://flask.palletsprojects.com/
- SQLAlchemy Documentation: https://www.sqlalchemy.org/
- Bootstrap CSS Framework: https://getbootstrap.com/

---

**For more information, see README.md and UPDATE_README.md**
