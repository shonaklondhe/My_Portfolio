#!/usr/bin/env python
import os
import glob

def view_emails():
    print("EMAIL VIEWER - Contact Form Messages")
    print("=" * 50)
    
    email_folder = "sent_emails"
    if not os.path.exists(email_folder):
        print("ERROR: No emails folder found")
        return
    
    email_files = glob.glob(f"{email_folder}/*.log")
    
    if not email_files:
        print("INFO: No emails found yet")
        return
    
    print(f"FOUND: {len(email_files)} email(s)")
    print()
    
    for i, email_file in enumerate(email_files, 1):
        print(f"EMAIL {i}:")
        print("-" * 30)
        
        try:
            with open(email_file, 'r', encoding='utf-8') as f:
                content = f.read()
                print(content)
        except Exception as e:
            print(f"ERROR reading {email_file}: {e}")
        
        print("-" * 30)
        print()

if __name__ == '__main__':
    view_emails()
