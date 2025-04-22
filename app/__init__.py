from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from config import Config

# Initialize extensions
db = SQLAlchemy()
csrf = CSRFProtect()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    csrf.init_app(app)

    from .routes import main_bp  # ensure correct import
    app.register_blueprint(main_bp)

    return app

# Debug helper
print("create_app defined?", 'create_app' in globals())