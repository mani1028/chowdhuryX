# ChowdhuryX - Technical Reference Document

## 🔧 Implementation Details

### Backend Architecture

#### Flask CSRF Protection Setup
```python
# app.py
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

def create_app(config_name=None):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))
    db.init_app(app)
    csrf.init_app(app)  # Initialize CSRF protection
```

#### Context Processor for CSRF Token
```python
@app.context_processor
def inject_config():
    from flask_wtf.csrf import generate_csrf
    return {
        'csrf_token': generate_csrf
    }
```

#### Secure File Upload
```python
from werkzeug.utils import secure_filename

@app.route('/apply-job', methods=['POST'])
def apply_job():
    if 'resume' in request.files:
        file = request.files['resume']
        if file and file.filename:
            # Sanitize filename
            original_filename = secure_filename(file.filename)
            filename = f"{datetime.now().timestamp()}_{original_filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
```

---

### Frontend Architecture

#### Toast Notification System
```javascript
// Create toast
new ToastNotification(title, message, type, duration)

// Quick helpers
showSuccessToast(title, message, duration)
showErrorToast(title, message, duration)
showWarningToast(title, message, duration)
showInfoToast(title, message, duration)
```

#### Page Loading Indicator
```html
<!-- In base.html -->
<div id="pageLoadingIndicator" class="page-loading-indicator">
    <div class="loading-bar"></div>
</div>

<script>
// Shows on link clicks, auto-hides on page load
document.addEventListener('click', function(event) {
    const link = event.target.closest('a[href]');
    if (link && /* internal link */) {
        document.getElementById('pageLoadingIndicator').classList.add('active');
    }
});
</script>
```

---

### CSS Architecture

#### Color System
```css
:root {
    /* Brand Colors */
    --brand-primary: #0066cc;
    --brand-primary-light: #0080ff;
    --brand-primary-dark: #0052a3;
    --brand-secondary: #ff6b35;
    --brand-secondary-light: #ff8456;
    --brand-secondary-dark: #e55a2b;
    
    /* Status Colors */
    --color-success: #28a745;
    --color-warning: #ffc107;
    --color-danger: #dc3545;
    --color-info: #17a2b8;
}
```

#### Responsive Grid
```css
/* 3-column grid for services */
.services-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
}

@media (max-width: 1024px) {
    .services-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 768px) {
    .services-grid {
        grid-template-columns: 1fr;
    }
}
```

#### Glassmorphism Modal
```css
.modal-content {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.5);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}
```

---

## 📊 File Structure

```
chowdhuryX/
├── app.py                          # Main Flask application
├── content_data.py                 # NEW: Centralized data config
├── models.py                       # Database models
├── config.py                       # Configuration
├── requirements.txt                # Dependencies
├── wsgi.py                         # WSGI entry point
├── static/
│   ├── css/
│   │   ├── global.css             # ENHANCED: Core styles
│   │   ├── navigation.css
│   │   ├── services.css
│   │   └── ...
│   ├── js/
│   │   ├── toast.js               # NEW: Toast system
│   │   ├── careers.js             # UPDATED: Toast integration
│   │   ├── main.js
│   │   └── ...
│   ├── images/
│   └── uploads/
├── templates/
│   ├── base.html                  # ENHANCED: JSON-LD + loading
│   ├── services.html              # ENHANCED: 3-col grid + modal
│   ├── service-detail.html        # ENHANCED: CTA section
│   ├── contact.html               # UPDATED: CSRF + toasts
│   ├── careers.html               # UPDATED: CSRF + toasts
│   └── ...
├── admin/                          # Admin module
├── instance/                       # Instance config
└── Documentation/
    ├── REFACTORING_COMPLETE.md    # Complete change log
    ├── IMPLEMENTATION_GUIDE.md    # Quick reference
    ├── PROJECT_SUMMARY.md         # Executive summary
    └── VERIFICATION_REPORT.md     # QA report
```

---

## 🔐 Security Implementation

### CSRF Protection Flow
```
User Request
    ↓
Check CSRF Token
    ↓ (Valid)
Process Request
    ↓
Response
```

### File Upload Security
```
File Received
    ↓
Sanitize Filename (secure_filename)
    ↓
Add Timestamp Prefix
    ↓
Validate Extension
    ↓
Save to Secure Directory
```

---

## 🎨 Design System

### Spacing Scale Usage
```html
<!-- Padding/Margin -->
<div style="padding: var(--spacing-lg);">  <!-- 24px -->
<div style="margin: var(--spacing-md);">   <!-- 16px -->
<div style="gap: var(--spacing-xl);">      <!-- 32px -->
```

### Color Usage
```html
<!-- Buttons -->
<button class="btn" style="background: var(--brand-primary);">

<!-- Text -->
<h1 style="color: var(--color-dark);">

<!-- Backgrounds -->
<div style="background: var(--color-gray-50);">
```

### Transition Usage
```css
/* Smooth interactions */
transition: all var(--transition-base);

/* Quick feedback */
transition: opacity var(--transition-fast);

/* Emphasis animations */
transition: transform var(--transition-slow);
```

---

## 📱 Responsive Design Breakpoints

| Device | Width | Grid | Approach |
|--------|-------|------|----------|
| Desktop | 1200px+ | 3 columns | Full experience |
| Tablet | 768px-1024px | 2 columns | Optimized layout |
| Mobile | < 768px | 1 column | Touch-friendly |

---

## ⚡ Performance Optimizations

### CSS Optimization
- ✅ CSS variables reduce file size
- ✅ GPU-accelerated transitions
- ✅ Minimal reflows with will-change
- ✅ Efficient selectors
- ✅ Minifiable structure

### JavaScript Optimization
- ✅ Event delegation
- ✅ Debounced handlers
- ✅ Minimal DOM manipulation
- ✅ Lazy loading ready
- ✅ Efficient animations

### Network Optimization
- ✅ Combined CSS files
- ✅ Minified JavaScript
- ✅ Optimized images
- ✅ CDN ready
- ✅ Cacheable resources

---

## 🧪 Testing Guide

### Manual Testing Checklist
- [ ] Contact form submits and shows success toast
- [ ] Career application uploads files securely
- [ ] Service modals open/close smoothly
- [ ] Page loading indicator shows on navigation
- [ ] Responsive layout works on mobile/tablet/desktop
- [ ] CSRF tokens appear in forms
- [ ] Color system applies throughout
- [ ] Transitions are smooth
- [ ] No console errors

### Automated Testing Template
```python
def test_csrf_protection():
    """Test CSRF token in forms"""
    response = client.get('/contact')
    assert b'csrf_token' in response.data

def test_secure_filename():
    """Test file upload sanitization"""
    filename = secure_filename('../../../etc/passwd')
    assert '/' not in filename

def test_service_data():
    """Test centralized data"""
    from content_data import get_service_details
    service = get_service_details('software-development')
    assert service is not None
    assert 'description' in service
    assert 'keywords' in service
```

---

## 🚀 Deployment Configuration

### Environment Variables
```bash
# Core
FLASK_ENV=production
SECRET_KEY=your-secure-key-here

# Database
DATABASE_URL=postgresql://user:pass@localhost/chowdhuryX

# Email (Optional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-password
```

### Production Server Setup
```bash
# Install production dependencies
pip install gunicorn
pip install python-dotenv

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app

# Or with environment file
gunicorn --env-file .env -w 4 -b 0.0.0.0:5000 wsgi:app
```

---

## 📈 Monitoring & Logging

### Application Logging
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Log form submissions
logger.info(f"Contact form submitted from {request.remote_addr}")

# Log file uploads
logger.info(f"Resume uploaded: {filename}")

# Log errors
logger.error(f"Job application error: {str(e)}")
```

### Performance Monitoring
- Monitor page load times
- Track form submission success rates
- Monitor file upload sizes
- Track CSRF token failures
- Monitor database queries

---

## 🔄 Maintenance Tasks

### Monthly
- [ ] Review error logs
- [ ] Check security updates
- [ ] Test backups
- [ ] Verify analytics
- [ ] Update dependencies

### Quarterly
- [ ] Audit user data
- [ ] Review security policies
- [ ] Performance tuning
- [ ] Content updates
- [ ] Database optimization

### Annually
- [ ] Security audit
- [ ] Architecture review
- [ ] Capacity planning
- [ ] Compliance check
- [ ] Technology evaluation

---

## 📚 API Reference

### Form Submission Handler
```python
@app.route('/contact', methods=['POST'])
def contact():
    """
    Handle contact form submission
    Expects: name, email, phone, subject, message
    Returns: JSON with success status and message
    """
```

### Service Detail Route
```python
@app.route('/services/<slug>')
def service_detail(slug):
    """
    Display service details with SEO metadata
    Parameters: slug (service identifier)
    Returns: Rendered template with service data
    """
```

### Career Application
```python
@app.route('/apply-job', methods=['POST'])
def apply_job():
    """
    Handle job application with file upload
    Expects: full_name, email, phone, position, experience_years, resume
    Returns: JSON with success status
    """
```

---

## 🎓 Learning Resources

### CSS Variables
- MDN: https://developer.mozilla.org/en-US/docs/Web/CSS/--*
- Complete guide to CSS custom properties

### Flask-WTF CSRF
- Docs: https://flask-wtf.readthedocs.io/
- CSRF protection implementation

### Glassmorphism
- Design trends and implementation
- CSS backdrop-filter property

### JSON-LD Schema
- https://json-ld.org/
- Schema.org vocabulary

### Toast Notifications
- UX best practices
- Implementation patterns

---

## ✅ Validation Checklist

Before deploying to production:
- [ ] All tests passing
- [ ] No console errors
- [ ] Security audit passed
- [ ] Performance benchmarks met
- [ ] Accessibility compliance verified
- [ ] Documentation updated
- [ ] Team training completed
- [ ] Rollback plan established
- [ ] Monitoring configured
- [ ] Backup tested

---

**Document Version**: 1.0
**Last Updated**: January 30, 2026
**Status**: CURRENT & COMPLETE
**Review Date**: Quarterly
