# 🚀 Deploy VCET Chatbot to Render.com

## Complete Step-by-Step Guide

### **Phase 1: Prepare Your GitHub Repository**

#### Step 1.1: Initialize Git (if not already done)
```bash
cd C:\Users\Vinith\Desktop\vcet-chatbot\VCET_Chatbot
git init
```

#### Step 1.2: Create `.gitignore` (already exists, but verify these are included)
```
venv/
__pycache__/
*.pyc
.env
Server/.env
.DS_Store
Thumbs.db
```

#### Step 1.3: Add files to Git
```bash
git add .
git commit -m "Initial VCET Chatbot setup"
```

#### Step 1.4: Create GitHub Repository
1. Go to [github.com](https://github.com)
2. Click **"New"** → Create a new repository
3. Name it: `vcet-chatbot`
4. Choose **Public** (easier for deployment)
5. Click **Create repository**

#### Step 1.5: Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/vcet-chatbot.git
git branch -M main
git push -u origin main
```

---

### **Phase 2: Set Up Render.com**

#### Step 2.1: Sign Up for Render
1. Go to [render.com](https://render.com)
2. Click **"Sign Up"** → Choose **GitHub**
3. Authorize Render to access your GitHub account
4. Complete the setup

#### Step 2.2: Create New Web Service
1. Click **"New +"** → Select **"Web Service"**
2. Connect your GitHub repository: Select `vcet-chatbot`
3. Click **"Connect"**

#### Step 2.3: Configure Deployment Settings

**Name:** `vcet-chatbot`

**Environment:** `Python 3.11`

**Build Command:**
```bash
cd Server && pip install -r requirements.txt
```

**Start Command:**
```bash
cd Server && gunicorn -w 1 -b 0.0.0.0:$PORT rag_chain:app
```

**Instance Type:** Free (or Starter if needed)

#### Step 2.4: Add Environment Variables
1. Scroll to **"Environment"** section
2. Click **"Add Environment Variable"** for each:

| Key | Value |
|-----|-------|
| `PINECONE_API_KEY` | `your_pinecone_api_key_here` |
| `PINECONE_ENV` | `us-east-1` |
| `GROQ_API_KEY` | `your_groq_api_key_here` |

#### Step 2.5: Deploy
1. Click **"Create Web Service"**
2. Wait for deployment (takes 2-5 minutes)
3. Once live, you'll see a URL: `https://vcet-chatbot-xxxx.onrender.com`

---

### **Phase 3: Verify Your Deployment**

#### Step 3.1: Test Your App
1. Open your Render URL in a browser
2. You should see the chatbot interface
3. Try sending a message

#### Step 3.2: Check Logs
- In Render dashboard, click your service
- View **"Logs"** to debug any issues

---

### **Phase 4: Auto-Deploy Updates**

Any time you push to GitHub, Render automatically redeploys:

```bash
# Make changes locally
git add .
git commit -m "Update chatbot features"
git push origin main

# Render automatically deploys within 1 minute
```

---

## 🔧 **Troubleshooting**

### **Issue: Build fails with "No module named..."**
- **Fix:** Ensure all imports in `rag_chain.py` are in `requirements.txt`

### **Issue: App crashes after deploy**
- **Check:** View Render **Logs** for error details
- **Common:** Missing environment variables (copy from Phase 2.4)

### **Issue: Frontend not loading**
- **Fix:** Verify `send_from_directory` path in `rag_chain.py` is correct
- Should serve from `../chatbot` directory

### **Issue: "Port already in use"**
- Render automatically assigns `$PORT` – code already handles this

---

## 📊 **Free Tier Limits (Render)**

- ✅ **Execution Time:** 750 hours/month (27 days continuous)
- ✅ **Free SSL certificate** (HTTPS)
- ✅ **Auto-deploy from GitHub**
- ⚠️ **Spins down** after 15 min of inactivity (free tier only)
- ⚠️ **Shared resources** (acceptable for testing)

---

## 🔐 **Security Best Practices**

1. **Never commit `.env`** to GitHub (already in `.gitignore`)
2. **Use environment variables** for all secrets (done in Phase 2.4)
3. **Rotate API keys** periodically
4. **Use strong GitHub authentication** (2FA recommended)

---

## 📱 **Share Your Live App**

Once deployed, share your Render URL:
```
https://vcet-chatbot-xxxx.onrender.com
```

---

## ✅ **Quick Checklist**

- [ ] GitHub repo created and code pushed
- [ ] Render account created
- [ ] Web Service connected to GitHub repo
- [ ] Environment variables set in Render
- [ ] Build command: `cd Server && pip install -r requirements.txt`
- [ ] Start command: `cd Server && gunicorn -w 1 -b 0.0.0.0:$PORT rag_chain:app`
- [ ] Deployment successful (check Render dashboard)
- [ ] Test chatbot at live URL
- [ ] Frontend loads and chat works

---

## 🎯 **Next Steps**

1. **Monitor Performance:** Check Render logs regularly
2. **Upgrade if needed:** Render offers paid plans if you exceed free limits
3. **Add CI/CD:** Render auto-deploys; no additional setup needed
4. **Scale up:** If chatbot gets popular, upgrade to paid instance

---

## 📞 **Need Help?**

- **Render Support:** [render.com/support](https://render.com/support)
- **GitHub Docs:** [docs.github.com](https://docs.github.com)
- **Flask Docs:** [flask.palletsprojects.com](https://flask.palletsprojects.com)
