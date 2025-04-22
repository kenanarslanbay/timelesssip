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
