#!/usr/bin/env python
"""
PythonAnywhere Deployment Setup Script
Run this script on PythonAnywhere after uploading your code
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(f"Output: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        return False

def setup_deployment():
    """Set up Django project for PythonAnywhere deployment"""
    
    print("🚀 Setting up Django project for PythonAnywhere deployment")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Error: manage.py not found. Please run this script from your project root directory.")
        sys.exit(1)
    
    # Install requirements
    if not run_command("pip install -r requirements.txt", "Installing requirements"):
        print("⚠️  Warning: Some packages might not have installed correctly")
    
    # Run migrations
    run_command("python manage.py migrate", "Running database migrations")
    
    # Collect static files
    run_command("python manage.py collectstatic --noinput", "Collecting static files")
    
    # Create superuser (if needed)
    print("\n👤 Checking for superuser...")
    try:
        from django.core.management import execute_from_command_line
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
        
        import django
        django.setup()
        
        from django.contrib.auth.models import User
        if not User.objects.filter(is_superuser=True).exists():
            print("Creating superuser...")
            run_command(
                "python manage.py shell -c \"from django.contrib.auth.models import User; User.objects.create_superuser('shonak', 'shonaklondhe.it@gmail.com', 'shonak@1216')\"",
                "Creating superuser"
            )
        else:
            print("✅ Superuser already exists")
    except Exception as e:
        print(f"⚠️  Could not check/create superuser: {e}")
    
    # Create email directory
    email_dir = 'sent_emails'
    if not os.path.exists(email_dir):
        os.makedirs(email_dir)
        print(f"✅ Created {email_dir} directory")
    
    print("\n🎉 Deployment setup completed!")
    print("\n📋 Next steps:")
    print("1. Configure your WSGI file in PythonAnywhere Web tab")
    print("2. Set static files path: /home/shonak/My_Portfolio/staticfiles/")
    print("3. Set virtual environment path: /home/shonak/My_Portfolio/venv/")
    print("4. Click 'Reload' button")
    print("5. Visit your site: https://shonak.pythonanywhere.com")
    
    print("\n🔐 Admin access:")
    print("Username: shonak")
    print("Password: shonak@1216")
    print("URL: https://shonak.pythonanywhere.com/admin/")

if __name__ == '__main__':
    setup_deployment()
