# Timeless Sip Coffee Shop

A Flask web application for a coffee shop with menu, reservations, and contact features.

## Setup

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
export FLASK_APP=run.py
export FLASK_ENV=development
export SECRET_KEY=your-secret-key-here
```

4. Initialize the database:
```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

5. Run the application:
```bash
flask run
```

## Features

- Homepage with featured items
- Menu page with categorized items
- Coffee guide with brewing information
- Contact form for inquiries
- Reservation system
- About page with team information

## Project Structure

- `app/` - Main application package
  - `static/` - Static files (CSS, images)
  - `templates/` - HTML templates
  - `models.py` - Database models
  - `forms.py` - Form definitions
  - `routes.py` - Route handlers
- `config.py` - Configuration settings
- `run.py` - Application entry point 