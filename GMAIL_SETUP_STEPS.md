# 📧 Gmail Setup for Real Email Sending

## 🔧 Step 1: Enable Less Secure App Access

### Method A: Direct Link (Easiest)
1. **Go to**: https://myaccount.google.com/lesssecureapps
2. **Turn ON** "Less secure app access"
3. **Done!** ✅

### Method B: Through Google Account Settings
1. **Go to**: https://myaccount.google.com/
2. **Click** "Security" on the left
3. **Scroll down** to "Less secure app access"
4. **Turn it ON**

## 🔑 Step 2: Update Your Password

1. **Open**: `config/settings.py`
2. **Find this line**:
   ```python
   EMAIL_HOST_PASSWORD = 'your_gmail_password_here'
   ```
3. **Replace** with your actual Gmail password:
   ```python
   EMAIL_HOST_PASSWORD = 'your_actual_gmail_password'
   ```
4. **Save the file**

## 🧪 Step 3: Test Real Email Sending

1. **Restart Django server** (if running):
   ```bash
   # Stop server with Ctrl+C, then restart:
   python manage.py runserver 8001
   ```

2. **Test with our script**:
   ```bash
   python test_email.py
   ```

3. **Check your Gmail inbox** - you should receive the test email!

## 🌐 Step 4: Test Contact Form

1. **Go to**: http://127.0.0.1:8001/contact/
2. **Fill out form** with test data
3. **Submit**
4. **Check Gmail inbox** for the contact form email

## 🚨 Troubleshooting

### If "Less Secure Apps" option is not available:
- You might have 2FA enabled
- Try using App Password instead (more complex)
- Or use a different email service

### If you get "Authentication failed":
- Double-check your Gmail password
- Make sure "Less secure app access" is ON
- Try waiting a few minutes after enabling it

### If emails don't arrive:
- Check Gmail spam folder
- Verify the email address is correct
- Try sending to a different email first

## ✅ Success Indicators

**You'll know it's working when:**
- ✅ No errors in terminal when submitting contact form
- ✅ Success message appears on contact page
- ✅ Email appears in your Gmail inbox
- ✅ Contact message is saved in Django admin

## 🔄 Fallback: Switch Back to Console

If you have issues, you can always switch back to console mode temporarily:

```python
# In settings.py, change:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# To:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

## 🎯 Quick Setup Summary

1. **Enable Less Secure Apps**: https://myaccount.google.com/lesssecureapps
2. **Update password** in `settings.py`
3. **Test**: `python test_email.py`
4. **Check Gmail inbox**
5. **Test contact form**: http://127.0.0.1:8001/contact/

Your portfolio contact form will be fully functional! 🚀
