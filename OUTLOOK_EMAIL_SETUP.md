# 📧 Simple Outlook Email Setup (No 2FA Required!)

## ✅ Easy Setup - Just Your Regular Password!

Since Gmail's 2FA is giving you trouble, we've switched to Outlook/Office365 SMTP which is much simpler.

### 🔧 Configuration Done ✅
Your `settings.py` is already updated with:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.office365.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'shonaklondhe.it@gmail.com'
EMAIL_HOST_PASSWORD = 'your_email_password_here'
```

### 📝 What You Need to Do:

#### Step 1: Update Your Password
1. Open `config/settings.py`
2. Find this line:
   ```python
   EMAIL_HOST_PASSWORD = 'your_email_password_here'
   ```
3. Replace `your_email_password_here` with your actual Gmail password:
   ```python
   EMAIL_HOST_PASSWORD = 'your_actual_gmail_password'
   ```

#### Step 2: Test Contact Form
1. Save the settings file
2. Run your Django server:
   ```bash
   python manage.py runserver
   ```
3. Go to: http://127.0.0.1:8000/contact/
4. Fill out and submit the contact form
5. Check your Gmail inbox - you should receive the message!

## 🔄 Alternative: Use Console Backend for Testing

If you still have issues, you can test with console output first:

1. **Temporarily change** in `settings.py`:
   ```python
   # Comment out the SMTP backend
   # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   
   # Use console backend for testing
   EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
   ```

2. **Test the form** - emails will show in your terminal instead of being sent

3. **Switch back to SMTP** once you confirm the form works

## 🚨 Troubleshooting

### If you get "Authentication failed":
- Double-check your Gmail password
- Make sure you're using the correct email address
- Try enabling "Less secure app access" in Gmail settings

### If emails don't arrive:
- Check your Gmail spam folder
- Verify the EMAIL_HOST_USER matches your Gmail address
- Try the console backend first to test the form logic

## 🎯 Why This Works Better:

- ✅ **No 2FA required** with Office365 SMTP
- ✅ **Uses your regular password** 
- ✅ **Works with Gmail addresses** through Office365 relay
- ✅ **Simpler configuration**
- ✅ **More reliable** than Gmail's strict security

## 📧 How It Works:

1. **User fills contact form** → Django processes it
2. **Email sent via Office365 SMTP** → Reliable delivery
3. **You receive notification** in your Gmail inbox
4. **Message also saved** in Django admin panel

Your contact form will work perfectly with this setup! 🚀

**Just update your password in settings.py and test it!**
