# 🚀 Production Deployment Guide

**Deploy Aeroseal ProposalAI to Railway + Custom Domain**

---

## Overview

**Architecture:**
- **Backend:** Railway (Flask API with OpenAI)
- **Frontend:** Static hosting with custom domain `aiduct.aidemo.live`
- **Database:** None (stateless API)
- **Storage:** Railway ephemeral storage for PDFs

---

## Part 1: Deploy Backend to Railway

### Step 1: Install Railway CLI (Optional but Recommended)

```bash
npm install -g @railway/cli
```

Or use the Railway web interface: https://railway.app

### Step 2: Prepare Your Backend

All necessary files are already created:
- ✅ `Procfile` - Tells Railway how to run the app
- ✅ `runtime.txt` - Specifies Python version
- ✅ `railway.json` - Railway configuration
- ✅ `requirements.txt` - Updated with gunicorn
- ✅ `.gitignore` - Prevents committing secrets

### Step 3: Initialize Git Repository (if not already done)

```bash
cd /Users/kunwar/abc/aiduct/prototype
git init
git add .
git commit -m "Initial commit: Aeroseal ProposalAI"
```

### Step 4: Deploy to Railway

**Option A: Using Railway CLI**

```bash
# Login to Railway
railway login

# Create new project
railway init

# Add environment variables
railway variables set OPENAI_API_KEY="your-openai-api-key-here"

# Deploy
railway up
```

**Option B: Using Railway Web Interface** (Recommended for beginners)

1. Go to https://railway.app and sign in
2. Click "New Project"
3. Select "Deploy from GitHub repo" (or "Empty Project" if no GitHub)
4. If using GitHub:
   - Connect your GitHub account
   - Create a new repo for this project
   - Push your code:
     ```bash
     git remote add origin your-github-repo-url
     git push -u origin main
     ```
   - Select the repo in Railway

5. If using "Empty Project":
   - Click "Deploy from local directory"
   - Railway CLI will upload your code

### Step 5: Configure Environment Variables in Railway

1. In Railway dashboard, go to your project
2. Click on "Variables" tab
3. Add the following variable:
   ```
   OPENAI_API_KEY=your-actual-openai-api-key
   ```
4. Click "Add" and Railway will automatically redeploy

### Step 6: Get Your Railway URL

1. After deployment, go to "Settings" tab
2. Under "Domains", you'll see a generated URL like:
   ```
   https://your-app-name.up.railway.app
   ```
3. **Copy this URL** - you'll need it for the frontend

### Step 7: Test Your Backend

Visit these URLs to verify:
- `https://your-app-name.up.railway.app/` - Should show the form
- Test the API by submitting a proposal

---

## Part 2: Set Up Frontend with Custom Domain

### Step 1: Create Production Frontend

We'll create a static HTML file that connects to your Railway backend:

```bash
cd /Users/kunwar/abc/aiduct/prototype
```

**File: `index-production.html`** (already created below)

This file will:
- Connect to Railway backend API
- Work from any static hosting (Vercel, Netlify, GitHub Pages, etc.)
- Use your custom domain `aiduct.aidemo.live`

### Step 2: Update Frontend API Endpoint

In the production HTML file (created below), update this line:

```javascript
const API_URL = 'https://your-railway-app.up.railway.app';
```

Replace with your actual Railway URL from Part 1, Step 6.

### Step 3: Choose Frontend Hosting

**Option A: Vercel (Recommended - Easiest)**

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy:
   ```bash
   cd /Users/kunwar/abc/aiduct/prototype
   vercel
   ```

3. Follow prompts:
   - Link to existing project? No
   - Project name: aeroseal-proposalai
   - Directory: `./` (current)
   - Override settings? No

4. Get your Vercel URL (e.g., `aeroseal-proposalai.vercel.app`)

**Option B: Netlify**

1. Install Netlify CLI:
   ```bash
   npm install -g netlify-cli
   ```

2. Deploy:
   ```bash
   netlify deploy --prod
   ```

3. Drag and drop `index-production.html` or specify directory

**Option C: GitHub Pages**

1. Create a new GitHub repo
2. Push `index-production.html` (rename to `index.html`)
3. Go to repo Settings > Pages
4. Enable GitHub Pages from main branch
5. Get URL: `https://yourusername.github.io/repo-name/`

### Step 4: Configure Custom Domain (aiduct.aidemo.live)

**For Vercel:**

1. In Vercel dashboard, go to your project
2. Click "Settings" > "Domains"
3. Add domain: `aiduct.aidemo.live`
4. Vercel will show you DNS records to add

**DNS Configuration:**

Add this record to your `aidemo.live` DNS:

```
Type: CNAME
Name: aiduct
Value: cname.vercel-dns.com
TTL: 3600
```

**For Netlify:**

1. In Netlify dashboard, go to Site Settings > Domain Management
2. Add custom domain: `aiduct.aidemo.live`
3. Netlify shows DNS records

**DNS Configuration:**

```
Type: CNAME
Name: aiduct
Value: your-site-name.netlify.app
TTL: 3600
```

**For GitHub Pages:**

1. In repo, create file `CNAME` with content: `aiduct.aidemo.live`
2. Add DNS record:

```
Type: CNAME
Name: aiduct
Value: yourusername.github.io
TTL: 3600
```

### Step 5: Add DNS Records

Go to your DNS provider for `aidemo.live` (Cloudflare, GoDaddy, Namecheap, etc.):

1. Log in to DNS management
2. Add the CNAME record from Step 4
3. Save changes
4. Wait 5-60 minutes for DNS propagation

### Step 6: Enable HTTPS

Most platforms (Vercel, Netlify, GitHub Pages) automatically provision SSL certificates via Let's Encrypt.

**Vercel:** Automatic
**Netlify:** Automatic
**GitHub Pages:** Enable in repo settings

---

## Part 3: Update Frontend to Connect to Railway

### Create Production-Ready Frontend

I'll create this file next with the Railway backend URL configurable.

**Key Changes:**
- API calls go to Railway backend
- CORS properly configured
- Production error handling
- Custom domain ready

---

## Part 4: Testing & Verification

### Test Checklist

- [ ] Backend deployed to Railway
- [ ] Railway environment variables set
- [ ] Backend accessible at Railway URL
- [ ] Frontend deployed to hosting service
- [ ] Custom domain `aiduct.aidemo.live` points to frontend
- [ ] HTTPS working on custom domain
- [ ] Frontend can call Railway backend API
- [ ] Full flow works: Form → AI → PDF generation → Download

### Test the Full Flow

1. Visit `https://aiduct.aidemo.live`
2. Fill out the proposal form
3. Click "Generate Professional Proposal"
4. Verify PDF downloads successfully
5. Check PDF content is correct

---

## Part 5: Post-Deployment Configuration

### Monitor Railway Backend

1. **Logs:** Railway dashboard > your project > Logs
2. **Metrics:** Check usage, requests, errors
3. **Scaling:** Railway auto-scales, but monitor costs

### Update OpenAI API Key (if needed)

```bash
railway variables set OPENAI_API_KEY="new-key"
```

Or via Railway dashboard > Variables > Edit

### Custom Domain for Railway Backend (Optional)

If you want a custom backend URL:

1. Railway dashboard > Settings > Custom Domain
2. Add domain (e.g., `api-aiduct.aidemo.live`)
3. Add DNS record:
   ```
   Type: CNAME
   Name: api-aiduct
   Value: your-app.up.railway.app
   TTL: 3600
   ```
4. Update frontend API_URL to custom domain

---

## Troubleshooting

### Backend Issues

**Railway deployment fails:**
- Check logs in Railway dashboard
- Verify `requirements.txt` has all dependencies
- Ensure `Procfile` is correct: `web: gunicorn app:app`

**500 errors:**
- Check Railway logs for Python errors
- Verify OPENAI_API_KEY is set correctly
- Check OpenAI API quota/billing

**CORS errors:**
- Ensure `flask-cors` is installed
- Backend has `CORS(app)` configured
- Railway backend allows frontend domain

### Frontend Issues

**Can't reach backend:**
- Check API_URL in frontend code
- Verify Railway backend is running
- Test backend URL directly in browser

**DNS not resolving:**
- Wait 30-60 minutes for DNS propagation
- Check DNS records with: `dig aiduct.aidemo.live`
- Verify CNAME points to correct hosting platform

**HTTPS not working:**
- Wait for SSL certificate provisioning (5-15 minutes)
- Check hosting platform SSL settings
- Ensure domain is verified

---

## Security Checklist

- [ ] OpenAI API key in environment variables (not in code)
- [ ] `.env` file in `.gitignore`
- [ ] CORS configured to allow only your frontend domain
- [ ] HTTPS enabled on both frontend and backend
- [ ] Rate limiting considered (for production scale)
- [ ] Error messages don't expose sensitive info

---

## Cost Estimates

### Railway (Backend)
- **Free Tier:** $5/month credit (should be enough for demo)
- **Paid:** ~$10-20/month for light usage
- **OpenAI API:** ~$10-50/month depending on usage

### Frontend Hosting
- **Vercel:** Free tier sufficient
- **Netlify:** Free tier sufficient
- **GitHub Pages:** Free

### Domain
- **aidemo.live:** You already own this
- **Subdomain:** Free

**Total Monthly Cost: $15-70** (mostly OpenAI API usage)

---

## Scaling Considerations

### For Production at Scale (1,500 dealers)

**Backend:**
- Upgrade Railway plan for higher limits
- Add Redis for caching
- Implement request queuing
- Add monitoring (Sentry, LogRocket)

**Storage:**
- Move PDFs to S3/Cloud Storage (Railway is ephemeral)
- Add database for proposal tracking
- Implement user authentication

**Performance:**
- Add CDN for static assets
- Optimize PDF generation
- Batch OpenAI requests
- Add load balancing

---

## Quick Reference Commands

### Railway CLI

```bash
# Login
railway login

# Deploy
railway up

# View logs
railway logs

# Set environment variable
railway variables set KEY=value

# Open dashboard
railway open
```

### Vercel CLI

```bash
# Deploy
vercel

# Deploy to production
vercel --prod

# View logs
vercel logs

# Add custom domain
vercel domains add aiduct.aidemo.live
```

### Git Commands

```bash
# Commit changes
git add .
git commit -m "Update"
git push

# Check status
git status
```

---

## Next Steps After Deployment

1. **Test thoroughly** with multiple scenarios
2. **Share URL** with CEO: `https://aiduct.aidemo.live`
3. **Monitor usage** in Railway dashboard
4. **Collect feedback** from test users
5. **Iterate** based on feedback
6. **Plan for scale** if approved for full deployment

---

## Support Resources

**Railway:**
- Docs: https://docs.railway.app
- Discord: https://discord.gg/railway
- Status: https://status.railway.app

**Vercel:**
- Docs: https://vercel.com/docs
- Support: https://vercel.com/support

**Debugging:**
- Backend logs: Railway dashboard
- Frontend errors: Browser console (F12)
- Network requests: Browser DevTools > Network

---

**Ready to deploy! Follow the steps and you'll have a production-ready demo at `https://aiduct.aidemo.live`** 🚀
