# Quick Testing Checklist

## Services Pages
- [ ] Visit `/services` - check header is white, service cards readable
- [ ] Click each service card - all 8 services should open detail pages:
  - [ ] AI Solutions (`/services/ai-solutions`)
  - [ ] BPO Services (`/services/bpo-services`)
  - [ ] Web Development (`/services/web-development`)
  - [ ] IT Consultant (`/services/it-consultant`)
  - [ ] Digital Marketing (`/services/digital-marketing`)
  - [ ] Software Development (`/services/software-dev`)
  - [ ] RPO Solutions (`/services/rpo-solutions`)
  - [ ] Recruitment (`/services/recruitment`)

## Industries Page
- [ ] Visit `/industries` - check header is white, text is dark and readable
- [ ] Hover over cards - should lift slightly with shadow
- [ ] Click industry cards - should navigate to industry detail pages

## Company Pages
- [ ] Visit `/why-choose-us` - header white, content readable
- [ ] Visit `/engagement-models` - header white, cards clear
- [ ] Visit `/trust-center` - header white, security info clear

## Legal Pages
- [ ] Visit `/cookies` - white header, dark readable text
- [ ] Visit `/terms` - white header, dark readable text
- [ ] Visit `/privacy-policy` - white header, dark readable text
- [ ] Visit `/cookie-settings` - test all 4 buttons:
  - [ ] Click "Accept All Cookies" - should show notification
  - [ ] Click "Reject All (Non-Essential)" - should toggle off checkboxes
  - [ ] Click "Save My Preferences" - should show success message
  - [ ] Click "Clear All Cookies" - should confirm and clear

## Forms & Functionality
- [ ] Visit `/contact`
  - [ ] Fill out form (name, email, subject, message)
  - [ ] Click "Send Message"
  - [ ] Should see success toast notification
  - [ ] Form should reset

- [ ] Visit `/careers`
  - [ ] Click "Apply Now" on any position
  - [ ] Modal should open
  - [ ] Fill form (name, email, phone, years, upload resume)
  - [ ] Submit form
  - [ ] Should see success toast
  - [ ] Modal should close

## Homepage Links
- [ ] Visit `/` (homepage)
  - [ ] Find "Why Choose Us" link - click should go to `/why-choose-us`
  - [ ] Find "View All Industries" button - click should go to `/industries`
  - [ ] All other links should work (not "#")

## Visual Checks
- [ ] All page headers on blue gradients have **white text**
- [ ] All body content has **dark gray text** (easy to read)
- [ ] No blurry or low-contrast text anywhere
- [ ] All buttons have hover effects
- [ ] Cards have subtle shadows and hover lift
- [ ] Forms have proper styling and alignment

## Browser Testing
Test in at least 2 browsers:
- [ ] Chrome/Edge
- [ ] Firefox
- [ ] Safari (if on Mac)

## Mobile Responsiveness (Optional)
- [ ] Resize browser to mobile width (< 768px)
- [ ] Check header text still visible
- [ ] Check cards stack vertically
- [ ] Check forms are usable on mobile

---

**If all checkboxes pass:** ✅ UI/UX fixes are successful!

**If any fail:** Check browser console for errors and ensure hard refresh (Ctrl+Shift+R)
