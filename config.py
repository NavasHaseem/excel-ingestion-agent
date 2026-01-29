"""Configuration for Excel Ingestion Agent"""
import os
from dotenv import load_dotenv

load_dotenv()

# Flask Configuration
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 5000))

# File Upload Configuration
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
OUTPUT_FOLDER = os.getenv('OUTPUT_FOLDER', 'output')
MAX_FILE_SIZE = int(os.getenv('MAX_FILE_SIZE', 10 * 1024 * 1024))  # 10MB default

# Allowed file extensions
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

# CORS Configuration
CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')

# API Configuration
API_TITLE = 'Excel Ingestion Agent'
API_VERSION = '1.0.0'
