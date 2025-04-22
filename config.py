# config.py
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'replace-with-strong-key'
    # Choose one or the other:
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('DATABASE_URL')
        or
        'sqlite:///' + os.path.join(basedir, 'app.db')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
