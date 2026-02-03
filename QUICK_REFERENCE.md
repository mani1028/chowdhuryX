# ChowdhuryX API - Quick Reference Card

## Endpoints by Category

### PUBLIC API (No Auth Required)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Homepage |
| `/about` | GET | About page |
| `/services` | GET | Services list |
| `/services/<slug>` | GET | Service detail |
| `/industries` | GET | Industries list |
| `/industries/<slug>` | GET | Industry detail |
| `/careers` | GET | Careers/jobs list |
| `/portfolio` | GET | Portfolio page |
| `/blog` | GET | Blog listing |
| `/blog/<slug>` | GET | Blog post detail |
| `/contact` | POST | Submit contact form |
| `/careers` | POST | Submit job application |
| `/blog/<id>/comment` | POST | Add comment |
| `/blog/<id>/like` | POST | Like blog post |
| `/comment/<id>/like` | POST | Like comment |
| `/faq` | GET | FAQ page |
| `/testimonials` | GET | Testimonials |
| `/privacy-policy` | GET | Privacy policy |
| `/terms` | GET | Terms of service |
| `/cookies` | GET | Cookie policy |

### ADMIN API (Authentication Required)

#### Authentication
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/admin/login` | POST | Admin login |
| `/admin/logout` | GET | Admin logout |

#### Dashboard & Analytics
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/admin/dashboard` | GET | Admin dashboard |
| `/admin/analytics` | GET | Analytics page |

#### Contacts Management
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/admin/contacts` | GET | List contacts |
| `/admin/contact/<id>` | GET | View contact |
| `/admin/contact/<id>/status` | POST | Update contact status |
| `/admin/contact/<id>/delete` | POST | Delete contact |

#### Careers Management
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/admin/careers` | GET | List applications |
| `/admin/career/<id>` | GET | View application |
| `/admin/career/<id>/status` | POST | Update application status |
| `/admin/career/<id>/delete` | POST | Delete application |

#### Blog Management
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/admin/blog` | GET | List blogs |
| `/admin/blog/new` | POST | Create blog |
| `/admin/blog/<id>` | GET | View blog |
| `/admin/blog/<id>/update` | POST | Update blog |
| `/admin/blog/<id>/publish` | POST | Publish blog |
| `/admin/blog/<id>/unpublish` | POST | Unpublish blog |
| `/admin/blog/<id>/delete` | POST | Delete blog |

#### Comments Management
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/admin/comments` | GET | List comments |
| `/admin/comment/<id>/spam` | POST | Mark as spam |
| `/admin/comment/<id>/delete` | POST | Delete comment |

#### Jobs Management
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/admin/jobs` | GET | List jobs |
| `/admin/jobs/new` | POST | Create job |
| `/admin/jobs/<id>` | GET | View job |
| `/admin/jobs/<id>/edit` | POST | Edit job |
| `/admin/jobs/<id>/delete` | POST | Delete job |
| `/admin/jobs/<id>/status` | POST | Toggle job status |
| `/admin/jobs/bulk-action` | POST | Bulk actions on jobs |

---

## Quick Test Scenarios

### Scenario 1: Complete User Journey (5 min)
```
1. GET  /              → Homepage loads
2. GET  /services      → Browse services
3. GET  /services/web  → View service detail
4. POST /contact       → Submit contact form
5. GET  /blog          → View blog
6. POST /blog/1/comment → Add comment
```

### Scenario 2: Admin Content Management (10 min)
```
1. POST /admin/login        → Login
2. GET  /admin/blog         → List posts
3. POST /admin/blog/new     → Create post
4. POST /admin/blog/1/publish → Publish
5. GET  /admin/blog/1       → View post
```

### Scenario 3: Admin Contact Processing (5 min)
```
1. POST /admin/login              → Login
2. GET  /admin/contacts          → View all
3. GET  /admin/contact/1         → View detail
4. POST /admin/contact/1/status  → Update status
```

### Scenario 4: Job Management (10 min)
```
1. POST /admin/login        → Login
2. GET  /admin/jobs         → List jobs
3. POST /admin/jobs/new     → Create job
4. POST /admin/jobs/1/status → Toggle status
5. POST /admin/jobs/bulk-action → Bulk action
```

---

## Common Parameters

### Contact Form
```
name: string (required)
email: string (required)
phone: string (optional)
subject: string (required)
message: string (required)
```

### Career Application
```
full_name: string (required)
email: string (required)
phone: string (optional)
position: string (required)
experience_years: integer (required)
resume: file (required)
cover_letter: string (optional)
```

### Blog Post
```
title: string (required)
content: string (required)
excerpt: string (optional)
category: string (optional)
author: string (optional)
featured_image: file (optional) - JPG, PNG, GIF, WebP
video_file: file (optional) - MP4, WebM, OGG, AVI, MOV, MKV, FLV, WMV
video_url: string (optional) - Embedded video URL (e.g., https://www.youtube.com/embed/VIDEO_ID)
status: string (draft/published)
```

### Job Posting
```
title: string (required)
location: string (required)
job_type: string (required)
  Options: Full-time, Part-time, Contract, Internship, Commission-based, 1099
department: string (required)
experience_required: string (required)
description: string (required)
requirements: string (required)
responsibilities: string (required)
salary_range: string (optional)
  Examples: "$80,000 - $120,000", "80k - 120k", "Competitive"
closes_at: date (optional)
status: string (active/inactive)
```

---

## Status Codes

| Code | Meaning | Action |
|------|---------|--------|
| 200 | OK | Success, check response body |
| 302 | Redirect | Follow redirect location |
| 400 | Bad Request | Check request parameters |
| 401 | Unauthorized | Login required |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Check ID/slug exists |
| 500 | Server Error | Check server logs |

---

## Request/Response Examples

### Contact Form Submission
```bash
curl -X POST http://localhost:5000/contact \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "name=John&email=john@example.com&subject=Hello&message=Test"
```

### Admin Login
```bash
curl -X POST http://localhost:5000/admin/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=password123"
```

### Create Blog Post
```bash
curl -X POST http://localhost:5000/admin/blog/new \
  -F "title=My Post" \
  -F "content=<p>Post content</p>" \
  -F "excerpt=Short desc" \
  -F "category=news" \
  -F "featured_image=@/path/to/image.jpg"
```

### Update Contact Status
```bash
curl -X POST http://localhost:5000/admin/contact/1/status \
  -H "Content-Type: application/json" \
  -d '{"status": "read"}'
```

---

## Postman Tips

### Auto-Save Cookies
1. Settings → **General**
2. **Keep cookies/redirects** → ON
3. Login cookies auto-saved

### Set Base URL Variable
1. Click **Variables** tab
2. Set `base_url = http://localhost:5000`
3. Use `{{base_url}}/endpoint` in requests

### Run Collection Tests
1. Click **Collection** name
2. Click **▶ Run** button
3. Select environment
4. Tests run automatically

### View Response Headers
1. Send request
2. Click **Headers** tab
3. Check `Set-Cookie`, `Content-Type`, etc.

---

## Database Reset (Development)

```bash
# Enter Python shell
python

# Reset database
from app import create_app, db
app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()
```

---

## Useful Filter Parameters

### List Endpoints Support:
```
?page=1            # Pagination
?status=new        # Filter by status
?department=Eng    # Filter by department
?export=true       # Export as CSV
```

### Examples:
```
/admin/contacts?status=new           # New contacts only
/admin/careers?page=2                # Page 2
/admin/jobs?department=Engineering   # Jobs in Eng dept
/admin/contacts?export=true          # CSV export
```

---

## Common Testing Flow

```
Step 1: Authentication
  └─ Login → Get session

Step 2: Public Pages
  └─ Browse website

Step 3: Form Submission
  └─ Submit contact/career form
  
Step 4: Admin Access
  └─ Verify form data in admin panel
  
Step 5: Admin Management
  └─ Edit/delete data in admin
  
Step 6: Verification
  └─ Confirm changes persisted
```

---

## Contact Support

- **Questions?** Check API_DOCUMENTATION.md
- **Testing Help?** See TESTING_GUIDE.md
- **Postman Issues?** Refer to TESTING_GUIDE.md → Troubleshooting
- **Bug Report?** See TESTING_GUIDE.md → Reporting Bugs

---

Last Updated: February 2026
Version: 1.0
