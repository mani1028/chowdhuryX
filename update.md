# 🏢 ChowdhuryX – Developer Guide (Internal)

This document explains the **UI/UX structure, responsibilities, and development rules**
for the ChowdhuryX company website.

This is a **real company project**, not a demo.

---

```text
chowdhuryX/
├── app.py                     # Flask entry point
├── requirements.txt            # Python dependencies
├── config.py                  # App configuration (env-based)
├── models.py                  # Shared DB models (Contact, Career, Blog)
├── README.md                  # Public project overview
├── UPDATE_README.md           # 🔥 Internal developer guide
│
├── admin/                     # 🔐 Admin module (isolated)
│   ├── __init__.py            # Admin blueprint init
│   ├── routes.py              # Admin routes (/admin/*)
│   ├── models.py              # Admin-only models
│   │
│   ├── templates/
│   │   ├── admin-login.html
│   │   ├── admin-dashboard.html
│   │   ├── admin-contacts.html
│   │   ├── admin-careers.html
│   │   └── admin-blog.html
│   │
│   └── static/
│       ├── css/
│       │   └── admin.css
│       └── js/
│           └── admin.js
│
├── templates/                 # 🌐 Public website pages
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   ├── industries.html
│   ├── portfolio.html
│   ├── careers.html
│   ├── contact.html
│   ├── blog.html
│   ├── blog-post.html
│   ├── faq.html
│   ├── testimonials.html
│   ├── privacy-policy.html
│   ├── terms.html
│   └── cookies.html
│
├── static/                    # 🎨 Public assets
│   ├── css/
│   │   ├── global.css
│   │   ├── home.css
│   │   ├── about.css
│   │   ├── services.css
│   │   ├── careers.css
│   │   └── responsive.css
│   │
│   ├── js/
│   │   ├── main.js
│   │   ├── contact.js
│   │   ├── careers.js
│   │   └── blog.js
│   │
│   └── images/
│       ├── logo/
│       ├── banners/
│       ├── services/
│       └── team/
│
├── .github/                   # 🧠 GitHub workflows & templates
│   ├── ISSUE_TEMPLATE/
│   │   ├── feature_request.yml
│   │   ├── bug_report.yml
│   │   └── task.yml
│   ├── pull_request_template.md
│   └── CODEOWNERS
│
├── .gitignore
└── venv/                      # ❌ Local only (ignored)
```



## 🎯 PROJECT GOAL

- Corporate / MNC-style company website
- Built using **HTML, CSS, JS, Python (Flask)**
- Scalable for admin panel & future client dashboard
- Clean separation between **Public Site** and **Admin**

---

## 🌐 PUBLIC WEBSITE PAGES

| Page | File |
|---|---|
Home | `templates/index.html`
About Us | `templates/about.html`
Services | `templates/services.html`
Industries | `templates/industries.html`
Portfolio | `templates/portfolio.html`
Careers | `templates/careers.html`
Contact | `templates/contact.html`
Blog | `templates/blog.html`
Blog Post | `templates/blog-post.html`
FAQ | `templates/faq.html`
Testimonials | `templates/testimonials.html`
Legal | `templates/privacy-policy.html`, `terms.html`, `cookies.html`

---

## 🎨 UI / UX GUIDELINES

### Design Rules
- Corporate & clean (no flashy animations)
- Consistent spacing & typography
- Mobile-first responsive design
- One primary color + one accent color



### Header Navigation

Home | About | Services | Industries | Portfolio | Careers | Blog | Contact


### Footer
Privacy Policy | Terms | Cookies | Careers


---

## 🎨 CSS RULES

- `global.css` → layout, typography, variables  
- Page-specific CSS → ONLY for that page  
- Do NOT add page styles into `global.css`

---

## ⚙️ JAVASCRIPT RULES

- `main.js` → navbar, scroll, common UI
- Page JS → form handling, validation only
- No inline JS inside HTML

---

## 🔐 ADMIN PANEL

### Admin URLs
/admin
/admin/login
/admin/contacts
/admin/careers
/admin/blog


### Admin Responsibilities
- View contact form submissions
- View career applications
- Manage blog posts (Phase 2)

Admin code is fully isolated inside `/admin`.

---

## 👥 TEAM WORK RULES

- One page = one owner
- Do not modify other pages without discussion
- Shared files (`base.html`, `global.css`) need approval
- Admin code handled only by assigned dev

---

## 🔁 DEVELOPMENT FLOW

1. Create Issue (GitHub template)
2. Create feature branch
3. Develop assigned page/module
4. Create Pull Request
5. Fill PR checklist
6. Review → merge to `dev`
7. Release → `main`

---

## 🚫 STRICTLY AVOID

- Mixing admin & public code
- Inline CSS or JS
- Pushing directly to `main`
- Hardcoding secrets

---

## 🚀 FUTURE PHASES

- Admin authentication & roles
- Blog CRUD
- Client dashboard
- CI/CD & deployment automation

---

## ✅ FINAL NOTE

This structure and process must be followed
to maintain **company-level quality and scalability**.



# ✅ DEVELOPER ONBOARDING CHECKLIST

Use this checklist when **joining the project** 👇

## 🔹 Day 1 — Setup
- [ ] Clone the repository
- [ ] Install Python (recommended 3.10+)
- [ ] Create virtual environment
- [ ] Install dependencies from `requirements.txt`
- [ ] Run the project locally
- [ ] Verify homepage loads correctly

## 🔹 Day 2 — Understanding Structure
- [ ] Review folder structure
- [ ] Read UPDATE_README.md completely
- [ ] Understand public vs admin separation
- [ ] Identify your assigned pages/modules

## 🔹 Day 3 — Git & Workflow
- [ ] Understand branch strategy (`main`, `dev`, `feature/*`)
- [ ] Review PR template
- [ ] Review Issue templates
- [ ] Make a small test PR

## 🔹 Before First Real Task
- [ ] Confirm page ownership
- [ ] Get clarity on UI/UX expectations
- [ ] Ask questions early
- [ ] Avoid changing shared files

---



1️⃣ feat → Type of change

This tells what kind of work this commit contains.

Common types you should use:

Type	Meaning	When to use
feat	Feature	New functionality
fix	Bug fix	Fixing a bug
style	UI/CSS	Only visual changes
refactor	Refactor	Code improvement, no behavior change
chore	Maintenance	Config, setup, docs
docs	Documentation	README, comments