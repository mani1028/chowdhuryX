# Entry point for WSGI servers (Gunicorn, uWSGI, etc.)
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from app import create_app

# Create application
app = create_app()