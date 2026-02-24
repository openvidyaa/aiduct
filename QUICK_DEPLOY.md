# 🚀 Quick Deploy to Production

Deploy Aeroseal ProposalAI to **Railway** + **aiduct.aidemo.live** in 15 minutes.

---

## Prerequisites

- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Railway account ([Sign up](https://railway.app))
- Access to DNS settings for `aidemo.live`
- Vercel/Netlify account (or use GitHub Pages)

---

## Step 1: Deploy Backend to Railway (5 minutes)

### Option A: Using Railway Web Interface (Recommended)

1. **Go to Railway**: https://railway.app
2. **Create New Project** → "Deploy from GitHub repo"
3. **Connect GitHub** (if not already):
   - Create a new GitHub repo for this project
   - Push code:
     ```bash
     cd /Users/kunwar/abc/aiduct/prototype
     git remote add origin YOUR_GITHUB_REPO_URL
     git branch -M main
     git push -u origin main
     ```
4. **Select the repo** in Railway and deploy
5. **Add Environment Variable**:
   - Go to project → Variables tab
   - Add: `OPENAI_API_KEY` = `your-actual-openai-api-key`
   - Railway will auto-redeploy

6. **Get Railway URL**:
   - Go to Settings → Domains
   - Copy URL like: `https://aeroseal-production-abc123.up.railway.app`
   - **Save this URL** - you'll need it next

### Option B: Using Railway CLI

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
cd /Users/kunwar/abc/aiduct/prototype
railway login
railway init
railway variables set OPENAI_API_KEY="your-openai-api-key"
railway up

# Get URL
railway open
```

### ✅ Verify Backend is Running

Visit your Railway URL in browser - you should see the proposal form.

---

## Step 2: Update Production Frontend (2 minutes)

Edit `index-production.html` line 451:

```javascript
// Change this line:
const API_URL = 'https://your-railway-app.up.railway.app';

// To your actual Railway URL:
const API_URL = 'https://aeroseal-production-abc123.up.railway.app';
```

Save the file.

---

## Step 3: Deploy Frontend to Vercel (3 minutes)

### Install Vercel CLI (if not installed)

```bash
npm install -g vercel
```

### Deploy

```bash
cd /Users/kunwar/abc/aiduct/prototype
vercel

# Follow prompts:
# - Set up and deploy? Yes
# - Which scope? Choose your account
# - Link to existing project? No
# - Project name? aeroseal-proposalai
# - Directory? ./ (just press Enter)
# - Override settings? No
```

Vercel will give you a URL like: `https://aeroseal-proposalai.vercel.app`

### Deploy to Production

```bash
vercel --prod
```

---

## Step 4: Configure Custom Domain (5 minutes)

### Add Domain to Vercel

1. In Vercel dashboard, go to your project
2. **Settings** → **Domains**
3. **Add Domain**: `aiduct.aidemo.live`

Vercel will show you DNS records to add.

### Update DNS for aidemo.live

Go to your DNS provider (Cloudflare, GoDaddy, etc.) and add:

```
Type: CNAME
Name: aiduct
Value: cname.vercel-dns.com
TTL: 3600
```

**Wait 5-30 minutes** for DNS propagation.

### ✅ Verify

Visit: `https://aiduct.aidemo.live`

You should see the Aeroseal ProposalAI form.

---

## Step 5: Test End-to-End (3 minutes)

1. **Fill out the form** with sample data:
   ```
   Address: 123 Oak Street, Columbus, OH 43215
   Building Type: Single Family Home
   Square Footage: 2500
   Year Built: 1995
   HVAC Age: 15
   Summer Bill: $250
   Winter Bill: $300
   Duct Location: Attic
   Customer Name: John Doe
   Email: john@example.com
   Contractor: Test Contractor
   ```

2. **Click "Generate Professional Proposal"**
3. **Wait ~15-30 seconds** for AI to calculate
4. **Download PDF** and verify it looks professional

**If you see errors**:
- Check Railway logs for backend errors
- Ensure OPENAI_API_KEY is set correctly
- Verify API_URL in frontend points to Railway backend

---

## 🎉 You're Live!

Your app is now deployed at: **https://aiduct.aidemo.live**

### Next Steps

1. **Share with CEO**: Send the URL and demo the app
2. **Monitor usage**: Check Railway dashboard for logs
3. **OpenAI costs**: Monitor at https://platform.openai.com/usage
4. **Iterate**: Collect feedback and enhance

---

## Troubleshooting

### Backend Issues

**500 errors from Railway:**
```bash
# View logs
railway logs

# Common issues:
# - OPENAI_API_KEY not set → Add in Railway Variables
# - OpenAI quota exceeded → Check billing
# - Python dependencies → Check requirements.txt
```

### Frontend Issues

**Can't connect to backend:**
- Verify `API_URL` in `index-production.html` matches Railway URL
- Check CORS in Railway logs
- Test Railway backend directly: `https://your-railway-url.up.railway.app`

**DNS not resolving:**
```bash
# Check DNS propagation
dig aiduct.aidemo.live

# Should show CNAME pointing to Vercel
```

**HTTPS errors:**
- Wait 10-15 minutes for Vercel SSL provisioning
- Check Vercel dashboard → Domains → SSL status

---

## Alternative: Deploy Frontend to Netlify

If you prefer Netlify over Vercel:

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy
cd /Users/kunwar/abc/aiduct/prototype
netlify deploy --prod

# Add custom domain in Netlify dashboard
# DNS record:
# Type: CNAME
# Name: aiduct
# Value: your-site-name.netlify.app
```

---

## Cost Estimate

- **Railway**: $5-20/month (Free tier available)
- **OpenAI API**: $10-50/month (depends on usage)
- **Vercel**: Free tier (sufficient for demo)
- **Domain**: You already own aidemo.live

**Total: ~$15-70/month**

---

## Files Reference

- **Backend**: `/Users/kunwar/abc/aiduct/prototype/app.py`
- **Production Frontend**: `index-production.html`
- **Detailed Guide**: `DEPLOYMENT_GUIDE.md`
- **Demo Script**: `DEMO_GUIDE.md`

---

**Need help?** See `DEPLOYMENT_GUIDE.md` for detailed troubleshooting.
