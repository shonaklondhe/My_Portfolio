# 🔧 Email Troubleshooting Guide

## 🧪 **STEP 1: Test Contact Form (Console Mode)**

Your server is now running with console email backend. Let's test:

### Test the Form:
1. **Open browser**: http://127.0.0.1:8000/contact/
2. **Fill out contact form** with test data:
   - Name: Test User
   - Email: test@example.com
   - Subject: Test Message
   - Message: This is a test message
3. **Submit the form**
4. **Check your terminal** where Django is running - you should see the email content printed there

### What to Look For:
```
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: New Contact Form Submission: Test Message
From: shonaklondhe.it@gmail.com
To: shonaklondhe.it@gmail.com
Date: ...

Contact Form Submission

Name: Test User
Email: test@example.com
Subject: Test Message
Message: This is a test message
```

## 🔍 **STEP 2: Check What's Happening**

### If you see the email in terminal:
✅ **Form is working correctly!** The issue is with SMTP configuration.

### If you don't see anything:
❌ **Form has an issue.** Let's check the contact view.

## 🛠️ **STEP 3: Fix SMTP Configuration**

Once we confirm the form works, we'll switch to real email sending:

### Option A: Gmail with App Password (Most Reliable)
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'shonaklondhe.it@gmail.com'
EMAIL_HOST_PASSWORD = 'your_16_char_app_password'  # Not regular password!
```

### Option B: Gmail with Less Secure Apps (Easier)
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'shonaklondhe.it@gmail.com'
EMAIL_HOST_PASSWORD = 'your_regular_gmail_password'
```

**For Option B, you need to:**
1. Go to https://myaccount.google.com/security
2. Turn ON "Less secure app access"
3. Use your regular Gmail password

### Option C: Different Email Provider
```python
# Using a different email service
EMAIL_HOST_USER = 'your_other_email@outlook.com'
EMAIL_HOST_PASSWORD = 'your_outlook_password'
EMAIL_HOST = 'smtp-mail.outlook.com'
```

## 🎯 **Quick Fix Steps:**

### Step 1: Test Console Mode
- Server is running ✅
- Go to contact form and submit
- Check terminal for email output

### Step 2: Enable Less Secure Apps (Easiest)
1. Go to: https://myaccount.google.com/lesssecureapps
2. Turn it **ON**
3. Update settings.py:
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'shonaklondhe.it@gmail.com'
   EMAIL_HOST_PASSWORD = 'your_actual_gmail_password'
   ```

### Step 3: Test Real Email
- Submit contact form
- Check Gmail inbox (and spam folder!)

## 📧 **Common Issues & Solutions:**

### "Authentication failed"
- Wrong password
- 2FA enabled but no app password
- Less secure apps disabled

### "SMTPException"
- Wrong SMTP settings
- Network/firewall issue
- Email provider blocking

### "No emails received"
- Check spam folder
- Wrong recipient email
- SMTP working but emails not delivering

## 🚀 **Let's Test Now!**

1. **Go to**: http://127.0.0.1:8000/contact/
2. **Submit test form**
3. **Check terminal** for email output
4. **Report back** what you see!

If you see the email in terminal, we know the form works and just need to fix SMTP! 📧
