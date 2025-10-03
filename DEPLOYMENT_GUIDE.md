# 🚀 Portfolio Deployment Guide - Make Your Portfolio Live!

## 🌐 Option 1: GitHub Pages (Free & Easy)

### Step 1: Enable GitHub Pages
1. Go to your repository: https://github.com/shonaklondhe/My_Portfolio
2. Click **Settings** tab
3. Scroll down to **Pages** section
4. Under "Source", select **Deploy from a branch**
5. Choose **main** branch
6. Click **Save**

### Step 2: Your Live URL
Your portfolio will be live at:
```
https://shonaklondhe.github.io/My_Portfolio/
```

**Note**: GitHub Pages works best with static sites. For Django, you'll need a different hosting solution.

---

## 🌟 Option 2: Railway (Recommended for Django)

### Step 1: Prepare for Railway
1. **Install Railway CLI**:
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway**:
   ```bash
   railway login
   ```

3. **Create railway.json**:
   ```json
   {
     "$schema": "https://railway.app/railway.schema.json",
     "build": {
       "builder": "NIXPACKS"
     },
     "deploy": {
       "startCommand": "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn config.wsgi:application",
       "healthcheckPath": "/"
     }
   }
   ```

### Step 2: Update Requirements
Add to `requirements.txt`:
```txt
gunicorn==21.2.0
whitenoise==6.6.0
psycopg2-binary==2.9.7
```

### Step 3: Update Settings for Production
Add to `settings.py`:
```python
import os

# Production settings
if 'RAILWAY_ENVIRONMENT' in os.environ:
    DEBUG = False
    ALLOWED_HOSTS = ['*']
    
    # Database
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
    
    # Static files
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### Step 4: Deploy
```bash
cd c:\Users\shona\OneDrive\Desktop\Portfolio-ML
railway init
railway up
```

---

## 🔥 Option 3: Render (Free Tier Available)

### Step 1: Create render.yaml
```yaml
services:
  - type: web
    name: portfolio
    env: python
    buildCommand: "pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate"
    startCommand: "gunicorn config.wsgi:application"
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

### Step 2: Deploy on Render
1. Go to https://render.com/
2. Connect your GitHub repository
3. Create new **Web Service**
4. Select your `My_Portfolio` repository
5. Configure:
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn config.wsgi:application`
6. Click **Deploy**

---

## ⚡ Option 4: Vercel (For Static Export)

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Create vercel.json
```json
{
  "builds": [
    {
      "src": "config/wsgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "config/wsgi.py"
    }
  ]
}
```

### Step 3: Deploy
```bash
cd c:\Users\shona\OneDrive\Desktop\Portfolio-ML
vercel
```

---

## 🐳 Option 5: Docker + Any Cloud Provider

### Step 1: Create Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### Step 2: Create docker-compose.yml
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
```

### Step 3: Deploy to Cloud
- **DigitalOcean App Platform**
- **AWS ECS**
- **Google Cloud Run**
- **Azure Container Instances**

---

## 🎯 Recommended Deployment Steps

### For Beginners: Railway
1. **Easiest Django deployment**
2. **Free tier available**
3. **Automatic HTTPS**
4. **Database included**

### Quick Setup:
```bash
# 1. Add to requirements.txt
echo "gunicorn==21.2.0
whitenoise==6.6.0
dj-database-url==2.1.0" >> requirements.txt

# 2. Install Railway CLI
npm install -g @railway/cli

# 3. Deploy
railway login
railway init
railway up
```

## 🔧 Pre-Deployment Checklist

- [ ] Update `ALLOWED_HOSTS` in settings.py
- [ ] Set `DEBUG = False` for production
- [ ] Configure static files handling
- [ ] Set up database (PostgreSQL for production)
- [ ] Configure email settings with app password
- [ ] Test contact form functionality
- [ ] Run `python manage.py collectstatic`
- [ ] Run `python manage.py migrate`

## 🌐 Your Live Portfolio Features

Once deployed, your portfolio will have:
- ✅ **Professional URL** (e.g., `yourapp.railway.app`)
- ✅ **HTTPS security** (automatic)
- ✅ **Mobile responsive** design
- ✅ **Contact form** with email notifications
- ✅ **ML demo** functionality
- ✅ **GitHub project** links
- ✅ **Admin interface** for content management
- ✅ **Fast loading** with optimized assets

## 📊 Post-Deployment

### Update Your Resume/Profiles:
- Add live portfolio URL to resume
- Update LinkedIn profile
- Share on social media
- Add to GitHub profile README

### Monitor Your Portfolio:
- Check contact form submissions
- Monitor site performance
- Update projects regularly
- Add new blog posts

Your portfolio will be live and accessible to potential employers worldwide! 🌟

**Recommended**: Start with Railway for the easiest Django deployment experience.
