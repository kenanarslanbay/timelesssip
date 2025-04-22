# Timeless Sip

**A modern, responsive Flask web application for a specialty coffee shop.**

---

## 🚀 Project Overview

**Timeless Sip** is a full‑stack Flask application that showcases:

- **Home**: Hero banner + feature cards (About, Coffee Quiz, Contact)  
- **About Us**: Our coffee passion and sourcing story  
- **Coffees Menu**: List of coffee offerings (filtered to “Coffees” category)  
- **Coffee Quiz**: Interactive 3‑step quiz recommending the perfect brew  
- **Contact**: CSRF‑protected contact form powered by Flask‑WTF  

It uses Jinja2 templates (`app/templates`), static assets (`app/static`), and SQLAlchemy models (`app/models.py`) with Postgres (or SQLite fallback).

---

## 📋 Tech Stack

- **Backend**: Python 3.x, Flask, Flask‑SQLAlchemy, Flask‑WTF  
- **Database**: PostgreSQL (primary) or SQLite (`app.db`) fallback  
- **Templating**: Jinja2  
- **Styling**: Custom CSS (with a warm coffee palette) + Flickity for carousel  
- **Forms & Validation**: WTForms + `email_validator`

---

## 🔧 Prerequisites

- **Python 3.8+**  
- **pip**  
- **PostgreSQL** (tested on Postgres 14 via Homebrew)

---

## ⛳ Getting Started

1. **Clone this repo**  
   ```bash
   git clone https://github.com/yourusername/timelesssip.git
   cd timelesssip

2. **Create & activate a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt

4. **Set environment variables**  
   ```bash
   export SECRET_KEY='a-strong-secret-key'
   export DATABASE_URL='postgresql://user:pass@localhost:5432/coffee_db'

5. **Start PostgreSQL (if using Postgres)**  
   ```bash
   brew services start postgresql@14
   createdb -O your_pg_user coffee_db

6. **Initialize database & seed data**  
   ```bash
   brew services start postgresql@14
   createdb -O your_pg_user coffee_db
   python seed.py
  
7. **Run the application**  
   ```bash
   python run.py

