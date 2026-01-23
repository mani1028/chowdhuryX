import sys
import os

# CPANEL FIX: Use path of the current file, not os.getcwd()
project_root = os.path.dirname(os.path.abspath(__file__))

if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import the 'app' object from app.py
from app import app as application