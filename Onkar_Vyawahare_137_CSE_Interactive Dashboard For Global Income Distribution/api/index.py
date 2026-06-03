import sys
import os

# Add the project root to the path so we can import from 'backend'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.app import app

# This is the entry point for Vercel
# Vercel's Python runtime expects the Flask instance to be named 'app'
# and will look for it in this file.
