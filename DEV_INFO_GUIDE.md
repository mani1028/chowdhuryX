# Hidden Developer Info Easter Egg Guide

## What Was Added

A hidden Easter egg that displays your developer information (name "MANIKANTA CH") encoded in Base64. When developers visit your site and press **Ctrl+Shift+D**, a beautiful modal popup appears with developer credits.

## How It Works

### 1. **Files Created/Modified**

#### New File: `static/js/dev-info.js`
- Contains the Easter egg logic
- Your name is stored **Base64 encoded**: `TUFOSUtBTlRBIENI` = "MANIKANTA CH"
- Creates a modal dialog with developer info
- Listens for keyboard shortcut: **Ctrl+Shift+D**

#### Modified: `templates/base.html`
- Added script tag to load `dev-info.js` on every page
- Script loads automatically for all pages

### 2. **Encoding** (Base64)

Your name is stored as Base64 because:
- ✅ Not visible at first glance in source code
- ✅ Can be decoded by any developer in their console
- ✅ Still shows in developer tools (dev/console)
- ✅ Professional and elegant approach

**How to encode your own name:**
```javascript
// In browser console:
btoa("MANIKANTA CH")  // Returns: "TUFOSUtBTlRBIENI"

// To decode:
atob("TUFOSUtBTlRBIENI")  // Returns: "MANIKANTA CH"
```

---

## How to View It

### Method 1: Using Keyboard Shortcut (Easiest)
1. Go to any page on your website
2. Press **Ctrl+Shift+D** (Windows/Linux) or **Cmd+Shift+D** (Mac)
3. A beautiful modal popup appears with your developer info

### Method 2: Using Browser Console
1. Open Developer Tools: **F12** or **Right-click → Inspect → Console**
2. You'll see logged messages in the console:
   ```
   🔧 ChowdhuryX Developer Info
   Developer: MANIKANTA CH
   Press Ctrl+Shift+D to open hidden developer panel
   ```
3. You can also manually run in console:
   ```javascript
   atob("TUFOSUtBTlRBIENI")  // Shows: "MANIKANTA CH"
   ```

### Method 3: View HTML Source
1. Right-click on page → **View Page Source** (Ctrl+U)
2. Search for `dev-info.js` or `ENCODED_NAME`
3. Find: `const ENCODED_NAME = 'TUFOSUtBTlRBIENI';`

---

## What Developers See

### In Browser Console (F12 → Console tab):
```
🔧 ChowdhuryX Developer Info
Developer: MANIKANTA CH
Press Ctrl+Shift+D to open hidden developer panel
```

### When Pressing Ctrl+Shift+D:
A beautiful purple gradient modal appears showing:
- **Developer:** MANIKANTA CH
- **Project:** ChowdhuryX
- **Year:** 2026
- **Type:** Enterprise Web App
- **Built with:** Flask, PostgreSQL, JavaScript

---

## Customize It

To change the information shown, edit `static/js/dev-info.js`:

### Change Your Name
```javascript
// Replace this line:
const ENCODED_NAME = 'TUFOSUtBTlRBIENI';

// With your encoded name. Use btoa() in console:
const ENCODED_NAME = btoa('YOUR NAME');  // E.g., btoa('JOHN DOE')
```

### Change Modal Content
Find this section and edit:
```javascript
<div class="dev-info-row">
    <span class="dev-info-label">Developer:</span>
    <span class="dev-info-value">${developerName}</span>
</div>

<div class="dev-info-row">
    <span class="dev-info-label">Project:</span>
    <span class="dev-info-value">ChowdhuryX</span>
</div>
```

### Change Keyboard Shortcut
Current: `Ctrl+Shift+D`

To change it, find this in `dev-info.js`:
```javascript
if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key.toUpperCase() === 'D') {
```

Change `'D'` to another key:
- `'I'` = Ctrl+Shift+I
- `'X'` = Ctrl+Shift+X
- etc.

### Change Modal Colors
Find the style section and edit:
```javascript
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
// Change to any CSS gradient
```

---

## Security Note

⚠️ **This is NOT a security feature**
- Base64 encoding is NOT encryption
- Anyone can decode it in 2 seconds using: `atob("TUFOSUtBTlRBIENI")`
- It's just a **professional Easter egg** for developers to find

If you need actual **secret keys**, use:
- Environment variables (`.env`)
- Encrypted config files
- Server-side storage

---

## File Locations

| File | Purpose | Editable |
|------|---------|----------|
| `static/js/dev-info.js` | Easter egg logic and modal | ✅ Yes |
| `templates/base.html` | Loads the script | ⚠️ Only if you know what you're doing |

---

## Testing

1. Navigate to any page: `http://localhost:5000/`
2. Open browser console: **F12**
3. Should see your name logged
4. Press **Ctrl+Shift+D** → Modal appears
5. Press **Escape** or click outside → Modal closes

---

## Tips for Other Developers

Share the Easter egg with other team members:
- **Hint:** "There's a hidden developer panel on the website"
- **Clue:** "Try pressing Ctrl+Shift+D"
- **Easter egg:** Find encoded messages in `dev-info.js`

---

Questions? Edit `static/js/dev-info.js` directly or ask for guidance!
