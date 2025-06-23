# This file makes the config directory a Python package 

import os
from datetime import timedelta

class Config:
    # Security Settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change-in-production'
    WTF_CSRF_SECRET_KEY = SECRET_KEY  # Use same key for CSRF
    
    # Session Settings
    SESSION_TYPE = 'filesystem'  # Use filesystem sessions
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)
    SESSION_COOKIE_NAME = 'exampro_session'
    SESSION_COOKIE_SECURE = True  # Enable secure cookies for HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_FILE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'flask_session')
    SESSION_FILE_THRESHOLD = 500  # Maximum number of sessions stored in the filesystem
    
    # CSRF Settings
    WTF_CSRF_ENABLED = True
    WTF_CSRF_CHECK_DEFAULT = True
    WTF_CSRF_TIME_LIMIT = None  # No time limit for CSRF tokens
    WTF_CSRF_SSL_STRICT = True  # Enable strict SSL checking for CSRF
    WTF_CSRF_METHODS = ['POST', 'PUT', 'PATCH', 'DELETE']
    
    # MongoDB Settings
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/exampro'
    
    # Upload Settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'uploads')

__all__ = ['Config'] 