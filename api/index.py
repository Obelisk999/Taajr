import sys
import os

# Add the parent directory to the Python path so we can import app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

# Export the Flask app as 'app' for Vercel
# Vercel will look for an app object in this file
