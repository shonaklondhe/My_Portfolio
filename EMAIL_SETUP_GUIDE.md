# 📧 Email Setup Guide for Contact Form

## 🔧 Gmail App Password Setup

To receive contact form emails, you need to set up a Gmail App Password:

### Step 1: Enable 2-Factor Authentication
1. Go to your **Google Account settings**: https://myaccount.google.com/
2. Click **Security** in the left sidebar
3. Under "Signing in to Google", click **2-Step Verification**
4. Follow the steps to enable 2FA (if not already enabled)

### Step 2: Generate App Password
1. In Google Account settings, go to **Security**
2. Under "Signing in to Google", click **App passwords**
3. Select app: **Mail**
4. Select device: **Windows Computer** (or Other)
5. Click **Generate**
6. **Copy the 16-character password** (example: `abcd efgh ijkl mnop`)

### Step 3: Update Your Portfolio Settings
1. Open `config/settings.py`
2. Find this line:
   ```python
   EMAIL_HOST_PASSWORD = 'your_app_password_here'
   ```
3. Replace `your_app_password_here` with your actual app password:
   ```python
   EMAIL_HOST_PASSWORD = 'abcd efgh ijkl mnop'
   ```

### Step 4: Test Contact Form
1. Run your Django server: `python manage.py runserver`
2. Go to the Contact page
3. Fill out and submit the form
4. Check your Gmail inbox for the message

## 🚀 Alternative: Use Environment Variables (Recommended)

For security, use environment variables:

### Create .env file:
```bash
# Create .env file in your project root
echo "EMAIL_HOST_PASSWORD=your_app_password_here" > .env
```

### Update settings.py:
```python
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
```

### Install python-dotenv:
```bash
pip install python-dotenv
```

## 📱 Contact Form Features

Once configured, your contact form will:
- ✅ **Save messages** to database (admin panel)
- ✅ **Send email notifications** to shonaklondhe.it@gmail.com
- ✅ **Show success message** to users
- ✅ **Handle errors gracefully**

## 🔍 Troubleshooting

### "Authentication failed" error:
- Make sure 2FA is enabled
- Use App Password, not regular Gmail password
- Check for typos in the app password

### "SMTPException" error:
- Check internet connection
- Verify Gmail settings are correct
- Try generating a new app password

### Not receiving emails:
- Check Gmail spam folder
- Verify EMAIL_HOST_USER matches your Gmail
- Test with console backend first

## 🧪 Testing Setup

To test without real emails, temporarily use console backend:

```python
# In settings.py, comment out SMTP and use console:
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

This will show emails in your terminal instead of sending them.

## ✅ Quick Setup Checklist

- [ ] Enable 2FA on Gmail account
- [ ] Generate Gmail App Password
- [ ] Update EMAIL_HOST_PASSWORD in settings.py
- [ ] Test contact form
- [ ] Check Gmail inbox
- [ ] Verify admin panel shows messages

Your contact form will be fully functional once the app password is configured! 📧
