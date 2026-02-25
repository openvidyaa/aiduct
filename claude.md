# Aeroseal Job Management Platform - Project Documentation

**Last Updated:** 2026-02-25 (15:15 IST)
**Status:** Active Development - Step 0 complete, ready for Step 2+
**Production URL:** https://aiduct.vercel.app/
**Backend API:** https://aiduct-production.up.railway.app/

---

## 📋 Project Overview

AI-powered complete lifecycle management platform for Aeroseal duct sealing contractors. Transforms the entire job process from initial proposal through job completion and certification.

### Business Problem Solved
- **Pre-sale:** Generate professional proposals in 15 minutes (vs 2-3 hours manual)
- **Job Planning:** AI analyzes blueprints and creates intelligent execution plans
- **Execution:** Guide technicians through standardized process with real-time tracking
- **Post-job:** Auto-generate completion reports and official certificates

### Target Users
- Aeroseal contractors and dealers
- HVAC technicians in the field
- Building owners (customer portal access)

---

## 🏗️ Current Architecture

### Frontend
- **Platform:** Vercel (Static HTML/CSS/JavaScript)
- **Framework:** Vanilla JavaScript (no build step)
- **Repository:** https://github.com/openvidyaa/aiduct
- **Main File:** `index.html` (contains full lifecycle platform)

### Backend
- **Platform:** Railway (Python Flask)
- **Runtime:** Python 3.13.0
- **Server:** Gunicorn
- **Dependencies:**
  - Flask 3.0.0 + Flask-CORS
  - OpenAI SDK >= 1.50.0
  - ReportLab 4.0.9 (PDF generation)
  - python-dotenv

### AI Integration
- **Model:** GPT-4 (proposals, analysis, content generation)
- **Future:** GPT-4 Vision (blueprint analysis)
- **Provider:** OpenAI API

---

## 🔄 Complete Job Lifecycle (9 Steps)

### **Step 0: 🧠 AI Job Assessment & Planning** ✅ COMPLETE
**Status:** Production-ready
**Purpose:** Analyze blueprints/building data to create intelligent job execution plan
**Features:**
- Blueprint/photo upload (drag & drop) - **Optional**
- GPT-4 Vision analysis of duct layout
- Complexity scoring (1-10)
- Crew size recommendation (1-3 techs)
- Time estimation with zone breakdown
- Risk assessment (Low/Moderate/High)
- 5 strategic insights per job:
  - Duct layout assessment
  - Access considerations
  - Building age factors
  - Recommended sealing sequence
  - Equipment/crew requirements
- Dynamic pricing multiplier (1.0x-2.5x)
- Works with or without image upload (smart fallback)

**Technical Implementation:**
- Frontend: `step0-demo.html` (standalone demo) + integrated in `index.html`
- Backend: `/api/analyze-job` endpoint (app.py lines 77-108)
- AI Functions:
  - `analyze_blueprint_with_vision()` - GPT-4 Vision image analysis (lines 110-153)
  - `generate_job_plan()` - GPT-4 strategic job planning (lines 155-248)
- Image handling: Base64 encoding, supports JPG/PNG (max 10MB)
- Smart fallback: If Vision API fails or no image, generates plan from building data alone

**Key Features:**
- Image upload is optional (form validates on building data, not image)
- Drag & drop interface with preview
- PDF support removed (coming soon - needs better handling)
- Real-time analysis with loading states
- Professional results display with complexity gauge

---

### **Step 1: 📋 Generate Professional Proposal** ✅ WORKING
**Status:** Production-ready
**Purpose:** AI-powered energy savings proposals with ROI calculations
**Features:**
- Building information form (address, type, sqft, year)
- HVAC system details (age, type, energy bills)
- Duct system information
- AI calculates:
  - Current leakage percentage
  - Expected savings percentage
  - Annual energy cost savings
  - Project cost estimate
  - Payback period
  - 10-year cumulative savings
  - CO₂ reduction
- Professional PDF proposal generation
- Executive summary, process description, environmental impact

**Backend Endpoint:** `/api/generate-proposal`
**PDF Generator:** `proposal_generator.py`
**File:** index.html lines 345-532

---

### **Step 2: ✅ Pre-Job Safety Checklist** 🚧 PLACEHOLDER
**Status:** Shell only (Coming Soon badge)
**Purpose:** Digital safety verification and equipment readiness
**Planned Features:**
- Safety equipment verification (PPE, ventilation, fire extinguisher)
- Customer walkthrough and expectations setting
- Equipment inventory check (Aeroseal machine, hoses, sealant)
- Site access and workspace preparation
- Photo documentation of initial site conditions
- Digital signature collection from property owner

**File:** index.html lines 534-562

---

### **Step 3: 📏 Before Measurements** 🚧 PLACEHOLDER
**Status:** Shell only
**Purpose:** Capture baseline duct leakage and system performance
**Planned Features:**
- Total duct leakage in CFM (Cubic Feet per Minute)
- System operating pressure measurements
- Temperature readings at supply and return vents
- Airflow measurements by room/zone
- Infrared thermal imaging capture points
- Auto-calculation of leakage percentage

**File:** index.html lines 564-592

---

### **Step 4: ⚙️ Live Aeroseal Process Tracker** 🚧 PLACEHOLDER
**Status:** Shell only
**Purpose:** Monitor 6-step sealing process in real-time
**Planned Features:**
- Step 1: Register sealing & system preparation (30 min)
- Step 2: System pressurization & baseline test (20 min)
- Step 3: Aerosol injection begins (1-2 hours)
- Step 4: Active sealing & leak reduction monitoring (2-4 hours)
- Step 5: Final verification & post-test (30 min)
- Step 6: System restoration & cleanup (45 min)
- Live CFM reduction graph visualization
- SMS updates to customer at each milestone

**File:** index.html lines 594-624

---

### **Step 5: 📸 Photo Documentation** 🚧 PLACEHOLDER
**Status:** Shell only
**Purpose:** Upload and organize before/during/after photos
**Planned Features:**
- Before: Duct system, equipment, workspace photos
- During: Aeroseal machine setup, sealing in progress
- After: Sealed vents, completed work, clean workspace
- Automatic timestamp and GPS tagging
- Upload from mobile camera or photo library
- AI-powered photo quality checks

**File:** index.html lines 626-654

---

### **Step 6: 📈 After Measurements & Results** 🚧 PLACEHOLDER
**Status:** Shell only
**Purpose:** Document post-sealing performance improvements
**Planned Features:**
- Final duct leakage CFM measurement
- Post-sealing system pressure readings
- Auto-calculation of % leakage reduction
- Before/after comparison charts
- Energy savings projections based on actual results
- Pass/fail verification (minimum 90% sealing recommended)

**File:** index.html lines 656-684

---

### **Step 7: 📄 AI-Powered Completion Report** 🚧 PLACEHOLDER
**Status:** Shell only
**Purpose:** Generate professional job completion documentation
**Planned Features:**
- Executive summary with before/after results
- Complete measurement data tables and charts
- Photo gallery with before/during/after sections
- Energy savings analysis and ROI validation
- Technician notes and observations
- Professional branded PDF with customer letterhead

**File:** index.html lines 686-714

---

### **Step 8: 🎖️ Official Certificate & Delivery** 🚧 PLACEHOLDER
**Status:** Shell only
**Purpose:** Issue Aeroseal certification and deliver all documents
**Planned Features:**
- Official Aeroseal completion certificate generation
- Warranty documentation and registration
- Automated email delivery to customer
- SMS notification with document links
- Customer portal access for future reference
- Integration with CRM for follow-up scheduling

**File:** index.html lines 716-744

---

## 📁 Project Structure

```
/Users/kunwar/abc/aiduct/prototype/
├── index.html                    # Main lifecycle platform (production)
├── step0-demo.html               # Step 0 standalone demo (AI Job Assessment)
├── index-lifecycle.html          # Backup copy of lifecycle platform
├── index-backup.html             # Additional backup
├── app.py                        # Flask backend API
├── proposal_generator.py         # PDF generation logic
├── requirements.txt              # Python dependencies
├── Procfile                      # Railway deployment config
├── runtime.txt                   # Python version (3.13.0)
├── vercel.json                   # Vercel deployment config
├── package.json                  # NPM package (forces static site detection)
├── .vercelignore                 # Exclude backend files from frontend deploy
├── .gitignore                    # Git exclusions
├── .env                          # Environment variables (local only)
├── claude.md                     # Project documentation (this file)
└── proposals/                    # Generated PDF proposals (gitignored)
```

---

## 🚀 Deployment Configuration

### Vercel (Frontend)
**File:** `vercel.json`
```json
{
  "framework": null,
  "installCommand": "npm install",
  "buildCommand": "npm run build",
  "outputDirectory": "."
}
```

**Key Settings:**
- `framework: null` - Disables auto-detection (prevents Flask detection)
- `outputDirectory: "."` - Serves files from root directory
- `.vercelignore` excludes Python files

### Railway (Backend)
**File:** `Procfile`
```
web: gunicorn app:app --bind 0.0.0.0:$PORT
```

**Environment Variables (Railway):**
- `OPENAI_API_KEY` - OpenAI API key for GPT-4 access
- `PORT` - Auto-assigned by Railway

**Key Settings:**
- Python 3.13.0 (runtime.txt)
- Gunicorn WSGI server
- Binds to Railway's dynamic PORT
- Health check on `/` endpoint

---

## 🔑 Key Technical Decisions

### 1. **Why Vanilla JavaScript?**
- No build step = faster iteration
- Easy to understand and modify
- Instant local testing (just open HTML)
- Vercel deployment issues with frameworks led to simpler approach

### 2. **Why Separate Frontend/Backend Repos?**
- Vercel auto-detection was confusing mixed Python/HTML
- Clear separation of concerns
- Frontend = static HTML on Vercel
- Backend = Python Flask on Railway
- Connected via CORS-enabled API calls

### 3. **Why Single-Page Index.html?**
- All 9 lifecycle steps in one file
- No routing complexity
- JavaScript shows/hides step content
- Easy to navigate with stepper UI
- Mobile-friendly scrolling

### 4. **Why ReportLab for PDF?**
- Pure Python (no external dependencies)
- Programmatic control over layout
- Works in Railway's containerized environment
- Alternative considered: WeasyPrint (too heavy)

### 5. **Why GPT-4 vs Fine-tuned Model?**
- Faster time to market (no training data needed)
- Flexibility to iterate on prompts
- Good enough for POC/MVP
- Can fine-tune later with real data

---

## 🐛 Issues Resolved

### Issue #1: Vercel Flask Detection Loop
**Problem:** Vercel kept detecting project as Flask, deployment failing
**Root Cause:** Framework detection runs before .vercelignore
**Solution:** Added `"framework": null` to vercel.json to disable auto-detection
**Date:** 2026-02-25

### Issue #2: F-String Formatting Errors
**Problem:** `Cannot specify ',' with 's'` errors in production
**Root Cause:** AI returning strings, formatted with `:,` thousand separator
**Solution:** Convert all numeric values to `float()` immediately after AI response
**Date:** 2026-02-24
**Files:** app.py lines 146-152, proposal_generator.py line 105

### Issue #3: Railway Port Binding Failure
**Problem:** Healthcheck failed on Railway deployment
**Root Cause:** Gunicorn not binding to Railway's dynamic PORT
**Solution:** Updated Procfile to `--bind 0.0.0.0:$PORT`
**Date:** 2026-02-24

### Issue #4: OpenAI API Proxies Error
**Problem:** `TypeError: Client.__init__() got an unexpected keyword argument 'proxies'`
**Root Cause:** Old OpenAI SDK version (1.12.0)
**Solution:** Upgraded to `openai>=1.50.0`
**Date:** 2026-02-24

### Issue #5: Mobile Layout Not Optimized
**Problem:** Form fields too small, poor touch targets on mobile
**Solution:** Added comprehensive mobile media queries (@media max-width: 768px)
**Date:** 2026-02-25

### Issue #6: Black Screen for Some Users
**Problem:** Other users seeing blank page when loading site
**Root Cause:** Vercel routing configuration
**Solution:** Simplified vercel.json routing rules
**Date:** 2026-02-25

### Issue #7: Image Upload Was Mandatory in Step 0
**Problem:** User couldn't analyze job without uploading an image
**Root Cause:** Button enable logic checked for uploaded image
**Solution:** Changed form validation to check building data instead (buildingType + sqft)
**Date:** 2026-02-25
**Impact:** Form now works with or without image upload (optional enhancement)

### Issue #8: PDF Upload Caused Errors in Step 0
**Problem:** Uploading PDF files caused analysis to fail
**Root Cause:** PDF preview failed, GPT-4 Vision can't directly process PDFs
**Solution:**
- Removed PDF from accepted file types
- Updated validation to only allow JPG/PNG
- Added "PDF support coming soon" message
**Date:** 2026-02-25
**Files:** step0-demo.html

### Issue #9: 403 Forbidden on Localhost
**Problem:** Accessing http://localhost:5000/step0-demo.html returned 403 error
**Root Cause:** Flask doesn't automatically serve HTML files from root directory
**Solution:** Use file:// URL for local testing: `file:///Users/kunwar/abc/aiduct/prototype/step0-demo.html`
**Date:** 2026-02-25
**Note:** For API testing, use Railway production endpoint from file:// URLs

---

## 📊 Current Status Summary

| Component | Status | Progress |
|-----------|--------|----------|
| Step 0: AI Job Assessment | ✅ Complete | 100% - Production ready |
| Step 1: Generate Proposal | ✅ Complete | 100% - Production ready |
| Step 2: Pre-Job Checklist | 🔲 Placeholder | 10% - Shell only |
| Step 3: Before Measurements | 🔲 Placeholder | 10% - Shell only |
| Step 4: Live Process Tracker | 🔲 Placeholder | 10% - Shell only |
| Step 5: Photo Documentation | 🔲 Placeholder | 10% - Shell only |
| Step 6: After Measurements | 🔲 Placeholder | 10% - Shell only |
| Step 7: AI Report Generator | 🔲 Placeholder | 10% - Shell only |
| Step 8: Certificate & Delivery | 🔲 Placeholder | 10% - Shell only |
| **Overall Platform** | **🚧 Active Development** | **33%** |

---

## 🎯 Next Steps (Priority Order)

### ✅ COMPLETED: Step 0 - AI Job Assessment
**Completed:** 2026-02-25
**Tasks:**
1. ✅ Create claude.md documentation
2. ✅ Update index.html to add Step 0 in lifecycle stepper
3. ✅ Build blueprint/photo upload interface (drag & drop)
4. ✅ Create backend `/api/analyze-job` endpoint
5. ✅ Implement GPT-4 Vision analysis
6. ✅ Generate AI Job Plan output (complexity, crew, time, risks, strategy)
7. ✅ Display results in professional report format
8. ✅ Test locally and deploy to production
9. ✅ Fix image upload optional issue
10. ✅ Fix PDF upload error (removed PDF support)
11. ✅ Integrate Step 0 into main lifecycle platform

### Next: Enhance Step 1 with Step 0 Data
**ETA:** 1-2 hours
- Pull complexity multiplier from Step 0 into pricing
- Show AI Job Plan summary in proposal PDF
- Link Step 0 analysis to Step 1 form

### Future: Build Steps 2-8 Sequentially
- Step 3: Before Measurements (measurement form + data capture)
- Step 6: After Measurements (before/after comparison)
- Step 7: AI Report Generator (comprehensive PDF)
- Step 2: Pre-Job Checklist (smart checklist generation)
- Step 4: Live Process Tracker (real-time monitoring)
- Step 5: Photo Documentation (image uploads)
- Step 8: Certificate & Delivery (email automation)

---

## 💡 Strategic Insights

### What Makes This Different?
1. **AI-First:** Not just tracking - intelligent analysis and planning
2. **Complete Lifecycle:** End-to-end from proposal to certificate
3. **Field-Ready:** Mobile-optimized for technicians on-site
4. **Competitive Moat:** Blueprint analysis is hard to replicate

### Value Proposition by User Type
**For Contractors:**
- 90% faster proposal generation
- Smarter job planning = fewer surprises
- Professional deliverables = higher close rates
- Data-driven pricing optimization

**For Technicians:**
- Clear execution roadmap for every job
- Reduced cognitive load (AI guides the process)
- Automated documentation
- Less paperwork, more wrench time

**For Customers:**
- Transparency (real-time updates)
- Professional experience
- Official certification
- Confidence in quality work

---

## 📝 Notes & Context

### Why Blueprint Analysis is Critical
- Hardest part of Aeroseal jobs is understanding duct complexity upfront
- Affects: crew size, time, pricing, risk, equipment needs
- Current process: Manual inspection + experience-based guessing
- AI opportunity: Analyze blueprints like a senior technician would

### Technology Choices Explained
- **GPT-4 Vision** chosen over custom CV model: faster iteration, good enough accuracy
- **Base64 encoding** for images (POC): simplest implementation, no storage setup needed
- **Railway + Vercel split**: Vercel's serverless has cold starts, Railway better for API
- **PDF generation server-side**: More control than browser-based solutions

### Testing Philosophy
- Test locally BEFORE pushing to avoid deployment loops
- Use `python3 -m http.server 8080` for quick local frontend testing
- Verify Railway API with `curl` before frontend integration

---

## 🔗 Important Links

- **Production Frontend:** https://aiduct.vercel.app/
- **Backend API:** https://aiduct-production.up.railway.app/
- **GitHub Repo:** https://github.com/openvidyaa/aiduct
- **Vercel Dashboard:** https://vercel.com/openvidyaa/aiduct
- **Railway Dashboard:** https://railway.app/ (check deployment logs)
- **OpenAI API Usage:** https://platform.openai.com/usage

---

## 📞 Handoff Information

**For next session:**
1. Read this claude.md file first
2. **Step 0 (AI Job Assessment) is complete and deployed! 🎉**
3. **Step 1 (Generate Proposal) is complete and deployed! 🎉**
4. Next priorities:
   - Option A: Build Steps 2-8 sequentially (recommended: Start with Step 3 - Before Measurements)
   - Option B: Enhance Step 1 to pull pricing multiplier from Step 0 data
   - Option C: Build more advanced features for existing steps
5. Test locally before deploying (use file:// URLs for frontend, Railway API for backend)
6. All placeholder steps (2-8) have detailed feature lists ready to implement

**Files to know:**
- `index.html` - Main frontend (all 9 steps, Step 0-8)
- `step0-demo.html` - Step 0 standalone demo (working)
- `app.py` - Backend API (add new endpoints here)
- `claude.md` - This file (update after major changes)

**What's Working:**
- Step 0: AI Job Assessment with GPT-4 Vision (optional image upload)
- Step 1: AI-powered proposal generation with PDF output
- Both deployed to production and fully tested

---

**End of Documentation**
*This file is a living document. Update it as the project evolves.*
