# 🚀 PythonAnywhere Deployment Guide

## 🌟 **Deploy Your Portfolio to PythonAnywhere**

PythonAnywhere is perfect for Django projects! Here's the complete step-by-step guide:

## 📋 **Step 1: Create PythonAnywhere Account**

1. **Go to**: https://www.pythonanywhere.com/
2. **Click**: "Pricing & signup"
3. **Choose**: "Beginner" (Free tier) - Perfect for portfolios
4. **Sign up** with your email
5. **Verify** your email address

## 🔧 **Step 2: Prepare Your Project**

### Update requirements.txt for production:
```txt
asgiref==3.9.2
Django==5.2.7
joblib==1.5.2
numpy==2.3.3
pandas==2.3.3
pillow==11.3.0
python-dateutil==2.9.0.post0
pytz==2025.2
scikit-learn==1.7.2
scipy==1.16.2
six==1.17.0
sqlparse==0.5.3
threadpoolctl==3.6.0
tzdata==2025.2
whitenoise==6.6.0
```

### Update settings.py for production:
Add to the end of `config/settings.py`:
```python
# Production settings for PythonAnywhere
import os

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Whitenoise for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Allowed hosts for PythonAnywhere
ALLOWED_HOSTS = ['shonak.pythonanywhere.com', 'localhost', '127.0.0.1']

# Database for production (SQLite is fine for portfolio)
# PythonAnywhere will use your existing db.sqlite3

# Email backend for production
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')
```

## 📤 **Step 3: Upload Your Code**

### Method A: Git (Recommended)
1. **Login to PythonAnywhere**
2. **Open "Bash" console**
3. **Clone your repository**:
   ```bash
   git clone https://github.com/shonaklondhe/My_Portfolio.git
   cd My_Portfolio
   ```

### Method B: File Upload
1. **Go to "Files" tab**
2. **Upload** your project folder
3. **Extract** if needed

## 🐍 **Step 4: Set Up Virtual Environment**

In PythonAnywhere Bash console:
```bash
# Navigate to your project
cd My_Portfolio

# Create virtual environment
python3.10 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## ⚙️ **Step 5: Configure Web App**

1. **Go to "Web" tab** in PythonAnywhere dashboard
2. **Click "Add a new web app"**
3. **Choose "Manual configuration"**
4. **Select "Python 3.10"**
5. **Click "Next"**

## 🔧 **Step 6: Configure WSGI File**

1. **In Web tab**, click on **WSGI configuration file** link
2. **Replace** the entire content with:

```python
import os
import sys

# Add your project directory to Python path
path = '/home/shonak/My_Portfolio'
if path not in sys.path:
    sys.path.insert(0, path)

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## 📁 **Step 7: Configure Static Files**

In the **Web** tab:

1. **Static files section**:
   - **URL**: `/static/`
   - **Directory**: `/home/shonak/My_Portfolio/staticfiles/`

2. **Media files section**:
   - **URL**: `/media/`
   - **Directory**: `/home/shonak/My_Portfolio/media/`

## 🗄️ **Step 8: Set Up Database**

In Bash console:
```bash
cd My_Portfolio
source venv/bin/activate

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create superuser
python manage.py createsuperuser --username shonak --email shonaklondhe.it@gmail.com
```

## 🌐 **Step 9: Configure Virtual Environment Path**

In **Web** tab:
1. **Virtualenv section**:
   - **Path**: `/home/shonak/My_Portfolio/venv/`

## 🚀 **Step 10: Launch Your Site**

1. **Click "Reload" button** in Web tab
2. **Your site will be live at**: `https://shonak.pythonanywhere.com`

## 🔧 **Troubleshooting**

### Common Issues:

**1. Import Error:**
- Check WSGI file path
- Verify virtual environment path
- Check Python version compatibility

**2. Static Files Not Loading:**
- Run `python manage.py collectstatic`
- Check static files configuration
- Verify STATIC_ROOT setting

**3. Database Issues:**
- Run migrations: `python manage.py migrate`
- Check database file permissions

**4. 500 Error:**
- Check error logs in Web tab
- Verify ALLOWED_HOSTS setting
- Check WSGI configuration

## 📊 **Post-Deployment Checklist**

### ✅ **Test Your Live Site:**
- [ ] Home page loads correctly
- [ ] All navigation links work
- [ ] Projects page displays properly
- [ ] Contact form submits successfully
- [ ] Admin panel accessible
- [ ] ML demo functions properly
- [ ] Resume downloads correctly
- [ ] Mobile responsive design works

### ✅ **Admin Access:**
- **URL**: `https://shonak.pythonanywhere.com/admin/`
- **Username**: `shonak`
- **Password**: `shonak@1216`

### ✅ **Contact Form:**
- Test contact form submission
- Check `sent_emails` folder for messages
- Verify admin panel shows contact messages

## 🎯 **Your Live Portfolio Features:**

Once deployed, your portfolio will have:
- ✅ **Professional URL**: `shonak.pythonanywhere.com`
- ✅ **HTTPS security** (automatic)
- ✅ **Working contact form**
- ✅ **ML price predictor demo**
- ✅ **GitHub project links**
- ✅ **Admin interface**
- ✅ **Mobile responsive design**
- ✅ **Fast loading** with optimized static files

## 🔄 **Updating Your Live Site**

To update your live site:
```bash
# In PythonAnywhere Bash console
cd My_Portfolio
git pull origin main
source venv/bin/activate
python manage.py collectstatic --noinput
python manage.py migrate
```

Then click **Reload** in Web tab.

## 💡 **Pro Tips:**

1. **Free tier limitations**: 1 web app, limited CPU seconds
2. **Custom domain**: Available with paid plans
3. **Database**: SQLite works fine for portfolios
4. **Monitoring**: Check Web tab for traffic stats
5. **Logs**: Use error logs for debugging

## 🎉 **Success!**

Your portfolio will be live at: **https://shonak.pythonanywhere.com**

Perfect for:
- ✅ **Job applications**
- ✅ **Client presentations**
- ✅ **Professional networking**
- ✅ **Showcasing your skills**

Your Django portfolio is now accessible worldwide! 🌍🚀
