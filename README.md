# 🌐 Django Website – Fully Responsive & Deployed on Render

[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://www.python.org/) 
[![Django](https://img.shields.io/badge/Django-4.2+-green)](https://www.djangoproject.com/) 
[![Render](https://img.shields.io/badge/Render-Cloud-orange)](https://render.com) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A professional Django website built with responsiveness, performance, and clarity in mind.  
This project includes multiple pages (Home, About, Sponsors, etc.) and is connected to a PostgreSQL database via Render.

---

## 📑 Table of Contents

- [🚀 Features](#-features)  
- [⚙️ Setup Instructions](#-setup-instructions)  
- [🧾 Environment Variables](#-environment-variables)  
- [📦 Deployment on Render](#-deployment-on-render)  
- [🧠 Static Files Configuration](#-static-files-configuration)  
- [🧰 Tech Stack](#-tech-stack)  
- [🏁 License](#-license)  

---

## 🚀 Features

- Mobile-optimized and fully responsive layout  
- PostgreSQL database integration  
- Clean, modular Django structure  
- Easy deployment using Render  
- Organized static and template directories  
- Professional folder structure for scalability  

---

## ⚙️ Setup Instructions

Follow these steps to run the project locally before deploying.

### 1️⃣ Clone the Repository

git clone https://github.com/yourusername/myproject.git  
cd myproject

### 2️⃣ Create a Virtual Environment

python -m venv venv

Activate it:  
Windows: venv\Scripts\activate  
macOS/Linux: source venv/bin/activate

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Run Database Migrations

python manage.py migrate

### 5️⃣ Run the Development Server

python manage.py runserver

Then open http://localhost:8000 in your browser.

---

## 🧾 Environment Variables

Create a file named `.env` in your project root and add:

SECRET_KEY=your_secret_key_here  
DEBUG=True  
DATABASE_URL=your_render_postgres_url_here

⚠️ **Never commit `.env` files to GitHub.** They’re already ignored in `.gitignore`.

---

## 📦 Deployment on Render

### Step 1: Add `render.yaml`

services:  
  - type: web  
    name: my-django-site  
    env: python  
    buildCommand: "pip install -r requirements.txt"  
    startCommand: "gunicorn myproject.wsgi:application"  
    envVars:  
      - key: DATABASE_URL  
        fromDatabase:  
          name: my-django-db  
          property: connectionString  
databases:  
  - name: my-django-db

### Step 2: Push Code to GitHub

git init  
git add .  
git commit -m "Initial commit"  
git branch -M main  
git remote add origin https://github.com/YOURUSERNAME/myproject.git  
git push -u origin main

### Step 3: Connect to Render

1. Go to https://render.com  
2. Click **“New Web Service”**  
3. Connect your GitHub repository  
4. Build command → pip install -r requirements.txt  
5. Start command → gunicorn myproject.wsgi:application  
6. Add your environment variables (SECRET_KEY, DATABASE_URL, etc.)  

Render will automatically build and deploy your Django site.

---

## 🧠 Static Files Configuration

In settings.py, make sure you have these lines:

STATIC_URL = '/static/'  
STATICFILES_DIRS = [BASE_DIR / 'main' / 'static']  
STATIC_ROOT = BASE_DIR / 'staticfiles'

### Whitenoise Setup

MIDDLEWARE = [  
    'django.middleware.security.SecurityMiddleware',  
    'whitenoise.middleware.WhiteNoiseMiddleware',  
    ...  
]

Then run:

python manage.py collectstatic

This ensures your CSS, JS, and image files are available in production.

---

## 🧰 Tech Stack

- Backend: Django  
- Frontend: HTML5 / CSS3 / JavaScript  
- Server: Production WSGI Server  
- Static Files: Whitenoise  
- Hosting: Render Cloud

✅ Run python manage.py check --deploy before pushing live

---

## 🏁 License

This project is open source under the MIT License.
