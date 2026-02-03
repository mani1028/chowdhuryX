# ChowdhuryX API Documentation

## Overview
ChowdhuryX is a corporate website with public-facing endpoints and a protected admin panel. This document covers all API endpoints for testing.

**Base URL:** `http://localhost:5000` (Development) or `https://yourdomain.com` (Production)

---

## Table of Contents
1. [Authentication](#authentication)
2. [Public Endpoints](#public-endpoints)
3. [Admin Endpoints](#admin-endpoints)
4. [Response Formats](#response-formats)
5. [Error Handling](#error-handling)
6. [Testing Guide](#testing-guide)

---

## Authentication

### Admin Login
**Endpoint:** `POST /admin/login`

**Description:** Authenticate admin user and create session

**Request:**
```
Content-Type: application/x-www-form-urlencoded
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| username | string | Yes | Admin username |
| password | string | Yes | Admin password |

**Example:**
```bash
curl -X POST http://localhost:5000/admin/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=your_password"
```

**Success Response (302 Redirect):**
- Redirects to `/admin/dashboard`
- Sets session cookie

**Error Response:**
```json
{
  "error": "Invalid username or password"
}
```

### Admin Logout
**Endpoint:** `GET /admin/logout`

**Description:** Clear admin session and logout

**Response:**
```
302 Redirect to /admin/login
```

---

## Public Endpoints

### 1. Homepage
**Endpoint:** `GET /`

**Response:** HTML (Featured blogs, services, testimonials)

---

### 2. Services
**Endpoint:** `GET /services`

**Response:** HTML (All services grid)

---

### 3. Service Detail
**Endpoint:** `GET /services/<slug>`

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | Service slug (e.g., "web-development") |

**Response:** HTML (Detailed service information)

---

### 4. Contact Form Submission
**Endpoint:** `POST /contact`

**Request:**
```
Content-Type: application/x-www-form-urlencoded
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| name | string | Yes | Contact name |
| email | string | Yes | Contact email |
| phone | string | No | Contact phone |
| subject | string | Yes | Message subject |
| message | string | Yes | Message body |

**Example:**
```bash
curl -X POST http://localhost:5000/contact \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "name=John Doe&email=john@example.com&subject=Inquiry&message=I have a question"
```

**Success Response:**
```
302 Redirect with success message
```

---

### 5. Careers/Job Applications
**Endpoint:** `GET /careers`

**Response:** HTML (Available job listings)

---

### 6. Submit Career Application
**Endpoint:** `POST /careers`

**Request:**
```
Content-Type: multipart/form-data
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| full_name | string | Yes | Applicant full name |
| email | string | Yes | Applicant email |
| phone | string | No | Applicant phone |
| position | string | Yes | Position applying for |
| experience_years | integer | Yes | Years of experience |
| resume | file | Yes | Resume file (.pdf, .doc, .docx) |
| cover_letter | string | No | Cover letter text |

**Example:**
```bash
curl -X POST http://localhost:5000/careers \
  -F "full_name=Jane Doe" \
  -F "email=jane@example.com" \
  -F "position=Developer" \
  -F "experience_years=3" \
  -F "resume=@/path/to/resume.pdf"
```

---

### 7. Blog Posts
**Endpoint:** `GET /blog`

**Response:** HTML (Published blog posts)

**Query Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| page | integer | Page number (default: 1) |

---

### 8. Blog Post Detail
**Endpoint:** `GET /blog/<slug>`

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | Blog post slug |

**Response:** HTML (Full blog post with comments)

---

### 9. Add Blog Comment
**Endpoint:** `POST /blog/<blog_id>/comment`

**Request:**
```
Content-Type: application/x-www-form-urlencoded
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| author | string | Yes | Comment author name |
| email | string | Yes | Author email |
| content | string | Yes | Comment text |

**Example:**
```bash
curl -X POST http://localhost:5000/blog/1/comment \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "author=John&email=john@example.com&content=Great post!"
```

---

### 10. Like Blog Post
**Endpoint:** `POST /blog/<blog_id>/like`

**Response:**
```json
{
  "success": true,
  "likes": 42
}
```

---

### 11. Like Comment
**Endpoint:** `POST /comment/<comment_id>/like`

**Response:**
```json
{
  "success": true,
  "likes": 5
}
```

---

### 12. Industries
**Endpoint:** `GET /industries`

**Response:** HTML (All industries)

---

### 13. Industry Detail
**Endpoint:** `GET /industries/<slug>`

**Response:** HTML (Industry specific information)

---

### 14. Portfolio
**Endpoint:** `GET /portfolio`

**Response:** HTML (Portfolio projects)

---

### 15. FAQ
**Endpoint:** `GET /faq`

**Response:** HTML (Frequently asked questions)

---

### 16. Testimonials
**Endpoint:** `GET /testimonials`

**Response:** HTML (Client testimonials)

---

### 17. Static Pages
**Endpoints:**
- `GET /privacy-policy` - Privacy policy
- `GET /terms` - Terms of service
- `GET /cookies` - Cookie policy
- `GET /engagement-models` - Engagement models
- `GET /why-choose-us` - Why choose us

---

## Admin Endpoints

> **Note:** All admin endpoints require authentication (session cookie from `/admin/login`)

### Dashboard

**Endpoint:** `GET /admin/dashboard`

**Response:** HTML (Admin dashboard with statistics)

---

### Contacts Management

#### List Contacts
**Endpoint:** `GET /admin/contacts`

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| page | integer | 1 | Page number |
| status | string | all | Filter by status (new/read/resolved) |
| export | boolean | false | Export as CSV |

**Response:** HTML or CSV file

---

#### View Contact
**Endpoint:** `GET /admin/contact/<contact_id>`

**Response:** HTML (Contact details)

---

#### Update Contact Status
**Endpoint:** `POST /admin/contact/<contact_id>/status`

**Request:**
```
Content-Type: application/json
```

**Body:**
```json
{
  "status": "read"
}
```

**Status Options:** `new`, `read`, `resolved`

**Response:**
```json
{
  "success": true
}
```

---

#### Delete Contact
**Endpoint:** `POST /admin/contact/<contact_id>/delete`

**Response:**
```json
{
  "success": true
}
```

---

### Careers/Applications Management

#### List Career Applications
**Endpoint:** `GET /admin/careers`

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| page | integer | 1 | Page number |
| status | string | all | Filter by status |
| export | boolean | false | Export as CSV |

**Status Options:** `applied`, `shortlisted`, `rejected`, `hired`

---

#### View Career Application
**Endpoint:** `GET /admin/career/<career_id>`

**Response:** HTML (Application details)

---

#### Update Career Status
**Endpoint:** `POST /admin/career/<career_id>/status`

**Request:**
```
Content-Type: application/json
```

**Body:**
```json
{
  "status": "shortlisted",
  "rating": 5,
  "notes": "Great candidate"
}
```

**Response:**
```json
{
  "success": true
}
```

---

#### Delete Career Application
**Endpoint:** `POST /admin/career/<career_id>/delete`

**Response:**
```json
{
  "success": true
}
```

---

### Blog Management

#### List Blog Posts
**Endpoint:** `GET /admin/blog`

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| page | integer | 1 | Page number |
| status | string | all | Filter by status (draft/published) |

---

#### Create Blog Post
**Endpoint:** `POST /admin/blog/new`

**Request:**
```
Content-Type: multipart/form-data
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| title | string | Yes | Blog title |
| content | string | Yes | Blog content (HTML supported) |
| excerpt | string | No | Short description |
| category | string | No | Category (default: news) |
| author | string | No | Author name |
| featured_image | file | No | Featured image (JPG, PNG, GIF, WebP) |
| video_file | file | No | Video file (MP4, WebM, OGG, AVI, MOV, MKV, FLV, WMV) |
| video_url | string | No | Embedded video URL (e.g., YouTube embed link: https://www.youtube.com/embed/VIDEO_ID) |

---

#### View Blog Post
**Endpoint:** `GET /admin/blog/<blog_id>`

**Response:** HTML (Blog edit form with comments)

---

#### Update Blog Post
**Endpoint:** `POST /admin/blog/<blog_id>/update`

**Request:**
```
Content-Type: application/json
```

**Body:**
```json
{
  "title": "Updated Title",
  "content": "Updated content",
  "excerpt": "New excerpt",
  "category": "news",
  "status": "draft"
}
```

**Response:**
```json
{
  "success": true
}
```

---

#### Publish Blog Post
**Endpoint:** `POST /admin/blog/<blog_id>/publish`

**Response:**
```json
{
  "success": true,
  "message": "Blog published successfully"
}
```

---

#### Unpublish Blog Post
**Endpoint:** `POST /admin/blog/<blog_id>/unpublish`

**Response:**
```json
{
  "success": true,
  "message": "Blog unpublished successfully"
}
```

---

#### Delete Blog Post
**Endpoint:** `POST /admin/blog/<blog_id>/delete`

**Response:**
```json
{
  "success": true
}
```

---

### Comments Management

#### List Comments
**Endpoint:** `GET /admin/comments`

**Query Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| page | integer | Page number |
| blog_id | integer | Filter by blog post |

---

#### Mark Comment as Spam
**Endpoint:** `POST /admin/comment/<comment_id>/spam`

**Response:**
```json
{
  "success": true,
  "status": "spam"
}
```

---

#### Delete Comment
**Endpoint:** `POST /admin/comment/<comment_id>/delete`

**Response:**
```json
{
  "success": true
}
```

---

### Jobs Management

#### List Jobs
**Endpoint:** `GET /admin/jobs`

**Query Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| page | integer | Page number |
| status | string | Filter by status (active/inactive) |
| department | string | Filter by department |

---

#### Create Job
**Endpoint:** `POST /admin/jobs/new`

**Request:**
```
Content-Type: application/x-www-form-urlencoded
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| title | string | Yes | Job title |
| location | string | Yes | Job location |
| job_type | string | Yes | Full-time, Part-time, Contract, Internship, Commission-based, 1099 |
| department | string | Yes | Department |
| experience_required | string | Yes | Required experience |
| description | string | Yes | Job description |
| requirements | string | Yes | Job requirements |
| responsibilities | string | Yes | Responsibilities |
| salary_range | string | No | Salary range (e.g. "$80,000 - $120,000", "80k - 120k", "Competitive") |
| status | string | No | active/inactive |
| closes_at | string | No | Closing date (YYYY-MM-DD) |

---

#### View Job
**Endpoint:** `GET /admin/jobs/<job_id>`

**Response:** HTML (Job details)

---

#### Edit Job
**Endpoint:** `POST /admin/jobs/<job_id>/edit`

**Request:** Same as Create Job

---

#### Delete Job
**Endpoint:** `POST /admin/jobs/<job_id>/delete`

**Response:**
```
302 Redirect to /admin/jobs
```

---

#### Toggle Job Status
**Endpoint:** `POST /admin/jobs/<job_id>/status`

**Response:**
```json
{
  "success": true,
  "status": "active",
  "message": "Job status changed to active"
}
```

---

#### Bulk Job Actions
**Endpoint:** `POST /admin/jobs/bulk-action`

**Request:**
```
Content-Type: application/x-www-form-urlencoded
```

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| action | string | activate, deactivate, delete |
| job_ids[] | array | Array of job IDs |

**Example:**
```bash
curl -X POST http://localhost:5000/admin/jobs/bulk-action \
  -d "action=activate&job_ids[]=1&job_ids[]=2&job_ids[]=3"
```

---

### Analytics

**Endpoint:** `GET /admin/analytics`

**Response:** HTML (Analytics dashboard with charts)

---

## Response Formats

### Success Response
```json
{
  "success": true,
  "message": "Operation completed",
  "data": {}
}
```

### Error Response
```json
{
  "success": false,
  "error": "Error description",
  "details": {}
}
```

### HTML Responses
Most endpoints return HTML templates. Check response `Content-Type: text/html` header.

---

## Error Handling

### Status Codes
| Code | Description |
|------|-------------|
| 200 | Success |
| 302 | Redirect |
| 400 | Bad Request |
| 401 | Unauthorized (Not logged in) |
| 403 | Forbidden (Insufficient permissions) |
| 404 | Not Found |
| 500 | Server Error |

### Common Errors
```json
{
  "error": "Invalid username or password"
}
```

```json
{
  "success": false,
  "message": "Blog is already published"
}
```

---

## Testing Guide

### 1. Setup
1. Install Postman or REST client
2. Import the provided `postman_collection.json`
3. Set environment variables in Postman

### 2. Basic Test Flow
```
1. POST /admin/login (Admin authentication)
2. GET /admin/dashboard (Verify authenticated)
3. GET /admin/contacts (List data)
4. POST /contact (Submit public form)
5. GET /admin/contacts (Verify submission)
```

### 3. Testing Checklist

#### Public Pages
- [ ] GET `/` loads homepage
- [ ] GET `/services` loads services
- [ ] GET `/services/<slug>` loads service detail
- [ ] GET `/careers` loads careers page
- [ ] GET `/blog` loads blog listing
- [ ] POST `/contact` submits contact form
- [ ] POST `/careers` submits job application

#### Admin Panel
- [ ] POST `/admin/login` authenticates
- [ ] GET `/admin/dashboard` requires auth
- [ ] GET `/admin/contacts` lists contacts
- [ ] POST `/admin/contact/<id>/status` updates status
- [ ] GET `/admin/blog` lists blogs
- [ ] POST `/admin/blog/new` creates blog
- [ ] POST `/admin/blog/<id>/publish` publishes blog
- [ ] GET `/admin/jobs` lists jobs
- [ ] POST `/admin/jobs/new` creates job

#### Edge Cases
- [ ] Logout clears session
- [ ] Invalid credentials rejected
- [ ] Missing required fields rejected
- [ ] File uploads validate type
- [ ] Pagination works correctly
- [ ] CSV export generates valid file

---

## Rate Limiting
No rate limiting currently implemented. Contact development team for production settings.

---

## CORS
CORS headers not configured. Same-origin requests only.

---

## Contact Support
For API issues, contact: support@chowdhuryX.com
