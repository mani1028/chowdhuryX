# ChowdhuryX API Testing - Setup & Quick Start

## For Your QA/Testing Team

This guide will get you testing in **5 minutes**. Follow these exact steps.

---

## Step 1: Install Postman (2 minutes)

### Windows/Mac:
1. Go to: https://www.postman.com/downloads/
2. Download appropriate version
3. Run installer and click **Install**
4. Launch Postman

### Linux:
```bash
sudo apt-get install postman
postman &
```

---

## Step 2: Get the Collection (1 minute)

You should have received these files:
- ✅ `postman_collection.json` 
- ✅ `API_DOCUMENTATION.md`
- ✅ `TESTING_GUIDE.md`
- ✅ `QUICK_REFERENCE.md`

Keep them in an accessible folder.

---

## Step 3: Import Collection to Postman (2 minutes)

1. **Open Postman**
2. Click **Import** button (top-left)
3. Click **Upload Files**
4. Select `postman_collection.json`
5. Click **Import**

✅ You should now see "ChowdhuryX API" in left sidebar

---

## Step 4: Configure Base URL (1 minute)

1. Click on **ChowdhuryX API** collection (left sidebar)
2. Click **Variables** tab (next to "Overview")
3. Find `base_url` variable
4. Set value to: `http://localhost:5000`
5. Click **Save** (Ctrl+S)

✅ Now all requests will work!

---

## Quick Test to Verify Setup

**Try This Request:**
1. Expand **ChowdhuryX API** → **Public Endpoints**
2. Click **Homepage** request
3. Click **Send** button
4. You should get **Status 200** with HTML content

✅ If you see 200, you're ready to test!

---

## Starting Your First Test

### Test 1: Visit Homepage
```
1. Collection → Public Endpoints → Homepage
2. Click Send
3. Expected: Status 200, HTML response
✅ PASS if status = 200
```

### Test 2: Submit Contact Form
```
1. Collection → Public Endpoints → Submit Contact Form
2. Click Send (pre-filled with sample data)
3. Expected: Status 200 or 302
✅ PASS if status = 200 or 302
```

### Test 3: Admin Login
```
1. Collection → Authentication → Admin Login
2. Edit username and password fields with your credentials
3. Click Send
4. Expected: Status 200 or 302, redirect to dashboard
✅ PASS if login succeeds and session saved
```

### Test 4: View Admin Dashboard
```
1. After login, Collection → Admin Dashboard → Dashboard
2. Click Send
3. Expected: Status 200, dashboard HTML
✅ PASS if you see dashboard (requires login from Step 3)
```

---

## Using the Postman Collection

### Organization
```
ChowdhuryX API
├── Authentication (2 requests)
├── Public Endpoints (15 requests)
├── Admin Dashboard (2 requests)
├── Contacts Management (6 requests)
├── Careers Management (5 requests)
├── Blog Management (8 requests)
├── Comments Management (3 requests)
└── Jobs Management (7 requests)
```

### How to Use Each Request

1. **Click folder** to expand and see requests
2. **Click request name** to view details
3. **Review the pre-filled fields** (parameters, body, etc.)
4. **Modify any fields** if needed
5. **Click Send** to execute
6. **Check response** at bottom:
   - Status code (200 = success, 404 = not found, etc.)
   - Response body (should match expected)
   - Response headers

---

## Common Testing Actions

### Sending a Form
```
Example: Submit Contact Form

1. Click request "Submit Contact Form"
2. You'll see:
   - Method: POST
   - URL: {{base_url}}/contact
   - Body: Pre-filled with sample data

3. Click Send
4. Check response status
```

### Viewing Lists
```
Example: List All Contacts

1. Click request "List Contacts"
2. You'll see:
   - Method: GET
   - URL: {{base_url}}/admin/contacts
   - Parameters: page=1, status=all

3. Click Send
4. Response shows contact list
```

### Creating Data
```
Example: Create New Blog Post

1. Click request "Create Blog Post"
2. You'll see:
   - Method: POST
   - Body: Form data with fields
   - Headers: multipart/form-data

3. Modify fields as needed
4. Click Send
5. Check response for success message
```

---

## Before Each Testing Session

### ✅ Checklist

- [ ] Server is running: `python app.py`
- [ ] Postman is open
- [ ] Collection is imported
- [ ] Base URL is set to `http://localhost:5000`
- [ ] You have admin credentials (username + password)
- [ ] Test database has sample data (or you're creating test data)

---

## During Testing

### Always Check:
1. **Status Code**: Is it what we expect?
   - 200 = Success
   - 302 = Redirect (OK for forms)
   - 404 = Not found
   - 500 = Error
   
2. **Response Body**: Does it have the expected data?

3. **Data Persistence**: Did the data save to database?
   - Check admin panel
   - Or check database directly

### Tips:
- 💡 Use QUICK_REFERENCE.md for quick lookups
- 💡 Follow TESTING_GUIDE.md for organized testing flow
- 💡 Read API_DOCUMENTATION.md for detailed info
- 💡 Keep notes of any issues found

---

## Reporting Issues

When you find a bug, include:

```
🐛 Bug Report Template

Title: [Brief description]

Endpoint: POST /admin/contact/1/delete
Method: POST
Status Code: 404 (Expected: 200)

Request:
- URL: {{base_url}}/admin/contact/1/delete
- Headers: Content-Type: application/json
- Body: {}

Response:
- Status: 404
- Body: {"error": "Contact not found"}

Expected:
- Status: 200
- Body: {"success": true}

Steps to Reproduce:
1. Login as admin
2. Go to /admin/contacts
3. Click delete on first contact
4. Observe: Contact still exists

Severity: HIGH 🔴 / MEDIUM 🟡 / LOW 🟢
```

---

## Troubleshooting

### Problem: Connection refused / Cannot reach server
```
❌ Error: Could not GET http://localhost:5000/

Solution:
1. Check if Flask server is running: python app.py
2. Check if it's running on correct port (default: 5000)
3. Try different port if 5000 is in use
4. Update base_url variable if using different port
```

### Problem: 401 Unauthorized
```
❌ Error: "Unauthorized"

Solution:
1. You must login first with POST /admin/login
2. Check credentials are correct
3. Verify session cookies are enabled in Postman
4. Try logout and login again
```

### Problem: 404 Not Found
```
❌ Error: "Not Found"

Solution:
1. Check endpoint URL is spelled correctly
2. Check the ID/slug exists (try ID: 1)
3. Verify base_url is correct
4. Item might have been deleted
```

### Problem: File Upload Failed
```
❌ Error: File not accepted or error message

Solution:
1. Check file format is allowed (PDF, DOC, etc.)
2. Check file actually exists on your computer
3. Use absolute file path
4. Check file is not too large
```

### Problem: CSRF Token Missing
```
❌ Error: "CSRF token missing"

Solution:
1. Go to Postman Settings
2. Find "General" or "Cookies" section
3. Enable "Automatically follow redirects"
4. Enable "Keep cookies across redirects"
5. Try again - cookies should auto-save from login
```

---

## File Reference

When you need help, use:

| Document | When to Use |
|----------|------------|
| **QUICK_REFERENCE.md** | Quick endpoint lookup, examples |
| **API_DOCUMENTATION.md** | Detailed endpoint info, parameters |
| **TESTING_GUIDE.md** | Full testing plan, test cases |
| **postman_collection.json** | Ready-made API requests |

---

## Sample Test Execution (15 minutes)

Follow this to complete a basic test:

```
Time: 0:00 - Start
├─ 0:00-0:05: Open Postman + Import collection
├─ 0:05-0:10: Setup base_url variable
├─ 0:10-0:13: Test GET / (Homepage)
├─ 0:13-0:15: Test POST /contact (Contact Form)
├─ 0:15-0:18: Test POST /admin/login (Login)
├─ 0:18-0:20: Test GET /admin/contacts (View contacts)
├─ 0:20-0:23: Verify submitted contact appears in list
└─ 0:23-0:25: Document results

Result: ✅ PASS - Basic workflow successful
Time: 0:25 - Done
```

---

## Next Steps

### Short Term (Day 1)
- [ ] Setup Postman with collection
- [ ] Run quick test (Homepage)
- [ ] Verify server connectivity
- [ ] Test admin login

### Medium Term (Week 1)
- [ ] Follow TESTING_GUIDE.md Phase 1-2
- [ ] Test all public endpoints
- [ ] Test form submissions
- [ ] Document any issues

### Long Term (Week 2-3)
- [ ] Complete all 10 testing phases
- [ ] Test edge cases
- [ ] Performance testing
- [ ] Final verification

---

## Useful Shortcuts

### Postman Shortcuts
```
Ctrl+S    = Save
Ctrl+/    = Toggle sidebar
Tab       = Auto-complete endpoint
Shift+Tab = Switch between tabs
Enter     = Send request (when in address bar)
```

### Server Commands
```
python app.py        = Start development server
Ctrl+C              = Stop server
python -i           = Interactive Python shell
flask run --debug   = Run with auto-reload
```

---

## Contact & Support

- **Stuck?** Check TESTING_GUIDE.md → Troubleshooting
- **Not sure how?** Check QUICK_REFERENCE.md
- **Need details?** Check API_DOCUMENTATION.md
- **Need examples?** Check postman_collection.json

---

## You're Ready! 🚀

You now have everything needed to test the ChowdhuryX API:

✅ Postman collection with 40+ pre-configured requests
✅ Complete API documentation
✅ Detailed testing guide with 10 phases
✅ Quick reference card
✅ This setup guide

**Start with STEP 1 above, then follow TESTING_GUIDE.md**

Good luck! 💪
