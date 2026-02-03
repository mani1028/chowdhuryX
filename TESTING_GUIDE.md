# ChowdhuryX - Complete Testing Guide

## Quick Start for Testers

### 1. Install Postman
- Download from: https://www.postman.com/downloads/
- Open Postman application

### 2. Import Collection
1. Click **Import** button (top left)
2. Select **Upload Files**
3. Choose `postman_collection.json` from the project root
4. Collection will be imported with all endpoints

### 3. Configure Environment

**Option A: Manually Set Base URL**
1. Open the collection
2. Click **Variables** tab
3. Set `base_url` to your server:
   - Local: `http://localhost:5000`
   - Production: `https://yourdomain.com`

**Option B: Create Postman Environment**
1. Click **Environments** (left sidebar)
2. Click **Create New**
3. Name it "ChowdhuryX"
4. Add variable:
   ```
   base_url = http://localhost:5000
   ```
5. Select this environment from dropdown (top right)

---

## Testing Workflow

### Phase 1: Authentication (Day 1)
```
✅ Test Admin Login
   POST /admin/login
   - Valid credentials → Success
   - Invalid credentials → Error
   - Check session cookie created
   
✅ Test Protected Routes
   GET /admin/dashboard (requires login)
   - Without login → Redirect to /admin/login
   - With login → Dashboard loads
   
✅ Test Logout
   GET /admin/logout
   - Session cleared
   - Redirect to login
```

**Test Cases:**

| Test | Endpoint | Method | Expected | Status |
|------|----------|--------|----------|--------|
| Valid Login | /admin/login | POST | 302 redirect to /admin/dashboard | [ ] |
| Invalid Login | /admin/login | POST | Error message | [ ] |
| Protected Route Access | /admin/dashboard | GET | Dashboard loads (if logged in) | [ ] |
| Logout | /admin/logout | GET | Redirect to /admin/login | [ ] |

---

### Phase 2: Public Pages (Day 1)
```
✅ Test Homepage
   GET /
   - All sections load
   - Featured blogs visible
   - Services grid loads
   - Testimonials load
   
✅ Test Services
   GET /services
   - All services listed
   - Grid layout works
   GET /services/<slug>
   - Service detail page loads
   - All information displays
   
✅ Test Blog
   GET /blog
   - Published posts listed
   - Pagination works
   GET /blog/<slug>
   - Full post loads
   - Comments section visible
   
✅ Test Careers
   GET /careers
   - Job listings display
   - Details accessible
```

**Test Cases:**

| Test | Endpoint | Expected | Status |
|------|----------|----------|--------|
| Homepage loads | GET / | 200 OK, HTML with blogs/services | [ ] |
| Services page | GET /services | Services grid loads | [ ] |
| Service detail | GET /services/web-development | Detailed info shown | [ ] |
| Blog listing | GET /blog | Published posts listed | [ ] |
| Blog detail | GET /blog/<slug> | Full post with comments | [ ] |
| Careers page | GET /careers | Job listings visible | [ ] |
| About page | GET /about | About content loads | [ ] |
| FAQ page | GET /faq | FAQ items load | [ ] |
| Testimonials | GET /testimonials | Testimonials display | [ ] |

---

### Phase 3: Form Submissions (Day 2)
```
✅ Test Contact Form
   POST /contact
   - Required fields validation
   - Email format validation
   - Success message appears
   - Data saved in database
   
✅ Verify in Admin
   GET /admin/contacts
   - Submitted contact appears
   - Status = "new"
   
✅ Test Career Application
   POST /careers
   - File upload works
   - All fields required
   - Resume file saved
   
✅ Verify in Admin
   GET /admin/careers
   - Application appears
   - Resume downloadable
   
✅ Test Blog Comment
   POST /blog/<id>/comment
   - Comment posted
   - Appears on blog page
   - Author/email saved
```

**Test Cases:**

| Test | Details | Status |
|------|---------|--------|
| Contact Form - Valid Submit | Name, email, subject, message | [ ] |
| Contact Form - Missing Name | Should error or require | [ ] |
| Contact Form - Invalid Email | Invalid format rejection | [ ] |
| Contact Form - Data in Admin | Verify appears in /admin/contacts | [ ] |
| Career Form - File Upload | Resume PDF upload works | [ ] |
| Career Form - Data Saved | Appears in /admin/careers | [ ] |
| Blog Comment | Comment posts and appears | [ ] |
| Blog Like | Like counter increments | [ ] |
| Comment Like | Like counter increments | [ ] |

---

### Phase 4: Admin Panel - Contacts (Day 2)
```
✅ List Contacts
   GET /admin/contacts
   - All contacts listed
   - Pagination works
   - Status filter works (new/read/resolved)
   - Export to CSV works
   
✅ View Contact
   GET /admin/contact/<id>
   - Contact details display
   - All fields visible
   
✅ Update Contact Status
   POST /admin/contact/<id>/status
   - Status changes: new → read → resolved
   - Update successful
   
✅ Delete Contact
   POST /admin/contact/<id>/delete
   - Contact removed from list
   - Success response
```

**Test Cases:**

| Test | Endpoint | Method | Expected | Status |
|------|----------|--------|----------|--------|
| List all contacts | /admin/contacts | GET | All contacts displayed | [ ] |
| Filter by status | /admin/contacts?status=new | GET | Only "new" contacts | [ ] |
| Paginate | /admin/contacts?page=2 | GET | Second page loads | [ ] |
| Export CSV | /admin/contacts?export=true | GET | CSV file downloaded | [ ] |
| View contact | /admin/contact/1 | GET | Full details shown | [ ] |
| Update status | /admin/contact/1/status | POST | Status updated | [ ] |
| Delete contact | /admin/contact/1/delete | POST | Contact removed | [ ] |

---

### Phase 5: Admin Panel - Careers (Day 3)
```
✅ List Applications
   GET /admin/careers
   - All applications listed
   - Filter by status
   - Export to CSV
   
✅ View Application
   GET /admin/career/<id>
   - Resume downloadable
   - All fields visible
   
✅ Rate Application
   POST /admin/career/<id>/status
   - Rate 1-5 stars
   - Add notes
   - Change status
   
✅ Bulk Actions
   - Select multiple
   - Activate/Deactivate
   - Delete multiple
```

**Test Cases:**

| Test | Endpoint | Method | Expected | Status |
|------|----------|--------|----------|--------|
| List applications | /admin/careers | GET | All listed | [ ] |
| Filter by status | /admin/careers?status=shortlisted | GET | Filtered results | [ ] |
| View application | /admin/career/1 | GET | Details + resume | [ ] |
| Rate/Add notes | /admin/career/1/status | POST | Status updated | [ ] |
| Export CSV | /admin/careers?export=true | GET | CSV file | [ ] |
| Delete application | /admin/career/1/delete | POST | Removed | [ ] |

---

### Phase 6: Admin Panel - Blog (Day 3)
```
✅ List Blog Posts
   GET /admin/blog
   - All posts listed
   - Filter: draft, published
   - Pagination works
   
✅ Create Blog Post
   POST /admin/blog/new
   - Title, content required
   - Image upload works
   - Saves as draft
   
✅ Edit Blog Post
   POST /admin/blog/<id>/update
   - Update title, content, excerpt
   - Category change
   - Status change
   
✅ Publish/Unpublish
   POST /admin/blog/<id>/publish
   POST /admin/blog/<id>/unpublish
   - Status changes
   - Publish timestamp set
   
✅ Delete Blog
   POST /admin/blog/<id>/delete
   - Post removed
   
✅ Manage Comments
   GET /admin/comments
   - All comments listed
   POST /admin/comment/<id>/spam
   - Mark spam
   POST /admin/comment/<id>/delete
   - Remove comment
```

**Test Cases:**

| Test | Endpoint | Method | Expected | Status |
|------|----------|--------|----------|--------|
| List blogs | /admin/blog | GET | All posts listed | [ ] |
| Filter draft | /admin/blog?status=draft | GET | Draft posts only | [ ] |
| Create blog | /admin/blog/new | POST | Post created as draft | [ ] |
| Upload featured image | /admin/blog/new | POST | Image saved | [ ] |
| View blog | /admin/blog/1 | GET | Edit form loads | [ ] |
| Update blog | /admin/blog/1/update | POST | Changes saved | [ ] |
| Publish blog | /admin/blog/1/publish | POST | Status = published | [ ] |
| Unpublish blog | /admin/blog/1/unpublish | POST | Status = draft | [ ] |
| Delete blog | /admin/blog/1/delete | POST | Post removed | [ ] |
| List comments | /admin/comments | GET | All comments | [ ] |
| Mark spam | /admin/comment/1/spam | POST | Status = spam | [ ] |
| Delete comment | /admin/comment/1/delete | POST | Comment removed | [ ] |

---

### Phase 7: Admin Panel - Jobs (Day 4)
```
✅ List Jobs
   GET /admin/jobs
   - All job postings listed
   - Filter by status
   - Filter by department
   - Pagination works
   
✅ Create Job
   POST /admin/jobs/new
   - Title, location, department required
   - Job type, experience, description
   - Optional: salary range, closing date
   
✅ Edit Job
   POST /admin/jobs/<id>/edit
   - Update all fields
   - Closing date change
   
✅ Toggle Status
   POST /admin/jobs/<id>/status
   - Active ↔ Inactive
   
✅ Bulk Actions
   POST /admin/jobs/bulk-action
   - Activate multiple
   - Deactivate multiple
   - Delete multiple
   
✅ Delete Job
   POST /admin/jobs/<id>/delete
   - Job removed
```

**Test Cases:**

| Test | Endpoint | Method | Expected | Status |
|------|----------|--------|----------|--------|
| List jobs | /admin/jobs | GET | All jobs listed | [ ] |
| Filter by status | /admin/jobs?status=active | GET | Active jobs only | [ ] |
| Filter by dept | /admin/jobs?department=Engineering | GET | Dept filtered | [ ] |
| View job | /admin/jobs/1 | GET | Job details | [ ] |
| Create job | /admin/jobs/new | POST | Job created | [ ] |
| Edit job | /admin/jobs/1/edit | POST | Changes saved | [ ] |
| Toggle status | /admin/jobs/1/status | POST | Status toggled | [ ] |
| Bulk activate | /admin/jobs/bulk-action | POST | Multiple activated | [ ] |
| Bulk delete | /admin/jobs/bulk-action | POST | Multiple deleted | [ ] |
| Delete job | /admin/jobs/1/delete | POST | Job removed | [ ] |

---

### Phase 8: Analytics (Day 4)
```
✅ View Analytics
   GET /admin/analytics
   - Top services chart
   - Top positions chart
   - Daily contacts trend
   - All data displays
```

**Test Cases:**

| Test | Expected | Status |
|------|----------|--------|
| Analytics page loads | Charts visible | [ ] |
| Top services shown | Service view counts | [ ] |
| Top positions shown | Application counts | [ ] |
| Daily contact trend | 30-day graph | [ ] |

---

### Phase 9: Error Handling & Edge Cases (Day 5)
```
✅ Test 404 Errors
   - Invalid service slug
   - Invalid blog slug
   - Invalid admin page
   
✅ Test 500 Errors
   - Check error page displays
   - Check error logging works
   
✅ Test Authentication Bypass
   - Try accessing admin without login
   - Try accessing others' data
   
✅ Test File Upload Validation
   - Invalid file types for resume
   - Invalid image formats
   - File size limits
   
✅ Test Data Validation
   - Empty required fields
   - Invalid email formats
   - XSS injection attempts
   - SQL injection attempts
```

**Test Cases:**

| Test | Method | Expected | Status |
|------|--------|----------|--------|
| Invalid service slug | GET /services/invalid | 404 page | [ ] |
| Invalid blog slug | GET /blog/invalid | 404 page | [ ] |
| Access admin without login | GET /admin/dashboard | Redirect to login | [ ] |
| Invalid email in contact | POST /contact | Email error | [ ] |
| No resume file | POST /careers | Error/required | [ ] |
| Invalid resume type | POST /careers | File type error | [ ] |
| XSS in contact name | POST /contact | Sanitized/escaped | [ ] |
| Missing required field | POST /contact | Form error | [ ] |

---

### Phase 10: Performance & Load Testing (Day 5)

```
✅ Basic Performance Tests
   - Homepage load time < 3 seconds
   - Admin pages load < 2 seconds
   - Large list pagination (100+ items)
   
✅ Concurrent Requests
   - Multiple simultaneous form submissions
   - Multiple blog views
   - Multiple admin logins
```

**Test Cases:**

| Test | Expected | Status |
|------|----------|--------|
| Homepage load time | < 3 seconds | [ ] |
| Admin dashboard load | < 2 seconds | [ ] |
| Large contact list | Pagination works smoothly | [ ] |
| CSV export | < 5 seconds | [ ] |

---

## How to Run Tests in Postman

### Method 1: Manual Testing
1. Open collection folder (e.g., "Authentication")
2. Click endpoint (e.g., "Admin Login")
3. Enter parameters/body
4. Click **Send**
5. Check response status and body
6. Repeat for all endpoints

### Method 2: Using Test Scripts
Many endpoints have built-in test scripts that run automatically after the request.

**To view test results:**
1. Send request
2. Click **Tests** tab (next to Body)
3. Results appear at bottom

### Method 3: Automated Test Suite (Advanced)
1. Click **Collection** (left sidebar)
2. Click play icon → **Run Collection**
3. Tests run automatically
4. View summary at end

---

## Common Issues & Troubleshooting

### Issue: 401 Unauthorized
**Solution:** Login first
```
1. Run POST /admin/login
2. Wait for response
3. Cookie saved automatically
4. Try protected route again
```

### Issue: 404 Not Found
**Solution:** Check endpoint URL and ID
- Verify base_url is correct
- Check ID exists (try ID 1 for first item)
- Check slug matches database

### Issue: CSRF Token Error
**Solution:** Ensure cookies enabled in Postman
- Cookies should auto-save from login
- Check in Postman Settings → Cookies

### Issue: File Upload Fails
**Solution:** Check file settings
- Use absolute file path
- Check file extension is allowed
- File should exist on your machine

### Issue: 500 Server Error
**Solution:** Check server logs
```
1. Look in terminal where Flask is running
2. Check error message
3. Ensure database is running
4. Check database migrations are applied
```

---

## Testing Checklist Summary

```
WEEK 1 - CORE FUNCTIONALITY
[ ] Authentication (Login/Logout)
[ ] Public Pages (Homepage, Services, Blog, etc.)
[ ] Form Submissions (Contact, Careers)
[ ] Admin Dashboard Access

WEEK 2 - ADMIN FEATURES
[ ] Contacts Management (List, View, Edit, Delete)
[ ] Careers Management (List, View, Rate, Delete)
[ ] Blog Management (Create, Edit, Publish, Delete)
[ ] Comments Management (List, Delete, Spam)

WEEK 3 - ADVANCED FEATURES
[ ] Jobs Management (Full CRUD)
[ ] Bulk Actions
[ ] Analytics Dashboard
[ ] CSV Exports

WEEK 4 - QUALITY ASSURANCE
[ ] Error Handling (404, 500)
[ ] Data Validation
[ ] Security Tests
[ ] Performance Tests
[ ] Cross-browser Testing
```

---

## API Response Examples

### Success Response (JSON)
```json
{
  "success": true,
  "message": "Operation completed successfully"
}
```

### Error Response (JSON)
```json
{
  "success": false,
  "error": "Descriptive error message"
}
```

### HTML Response
- Expected Content-Type: `text/html; charset=utf-8`
- Contains rendered template

---

## Database Verification

After form submissions, verify data in database:

### Check Contact Submission
```sql
SELECT * FROM contact ORDER BY created_at DESC LIMIT 1;
```

### Check Career Application
```sql
SELECT * FROM career ORDER BY created_at DESC LIMIT 1;
```

### Check Blog Post
```sql
SELECT * FROM blog ORDER BY created_at DESC LIMIT 1;
```

---

## Reporting Bugs

When you find an issue, report with:

1. **Endpoint:** `POST /admin/contact/1/status`
2. **Method:** POST
3. **Input:** `{"status": "invalid"}`
4. **Expected:** Error message
5. **Actual:** Status changed to invalid
6. **Severity:** High/Medium/Low
7. **Steps to Reproduce:**
   - Login as admin
   - Go to /admin/contacts
   - Click on a contact
   - Attempt to change status to "invalid"

---

## Support

- **API Docs:** See API_DOCUMENTATION.md
- **Postman Collection:** See postman_collection.json
- **Backend Issues:** Check terminal logs where Flask is running
- **Database Issues:** Verify database connection in .env file

---

## Environment Setup Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
python app.py

# Or with Flask CLI
flask run

# Run on specific port
flask run --port 5001

# Reset database (development only)
python
> from app import create_app, db
> app = create_app()
> with app.app_context():
>     db.drop_all()
>     db.create_all()
```

---

Good luck with testing! 🚀
