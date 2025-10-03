#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings

def test_email():
    print("Testing email functionality...")
    print(f"Email backend: {settings.EMAIL_BACKEND}")
    print(f"Default from email: {settings.DEFAULT_FROM_EMAIL}")
    
    try:
        print("\nSending test email...")
        send_mail(
            'Test Email from Portfolio',
            'This is a test email to verify the contact form is working.\n\nIf you see this in your terminal, the email system is configured correctly!',
            settings.DEFAULT_FROM_EMAIL,
            ['shonaklondhe.it@gmail.com'],
            fail_silently=False,
        )
        print("SUCCESS: Email sent successfully!")
        print("\nLOOK ABOVE: Check above for email content in console output!")
        
    except Exception as e:
        print(f"ERROR: Email failed: {e}")

if __name__ == '__main__':
    test_email()
