# WSGI Configuration for PythonAnywhere
# Copy this content to your WSGI configuration file on PythonAnywhere

import os
import sys

# Add your project directory to Python path
# IMPORTANT: Replace 'shonak' with your actual PythonAnywhere username
path = '/home/shonak/My_Portfolio'
if path not in sys.path:
    sys.path.insert(0, path)

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Optional: Add logging for debugging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("WSGI application loaded successfully")
