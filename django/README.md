# Django Project Setup Guide

This guide walks you through setting up a Django project with a virtual environment and a user application.

## Prerequisites
- Python 3.x installed
- pip package manager
- Basic knowledge of command line operations

## Setup Instructions

### 1. Create and Activate Virtual Environment
```bash
python -m venv virtualEnv
cd virtualEnv/Scripts
source activate  # On Windows use: activate
cd ../..
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Create Django Project and App
```bash
django-admin startproject mainProject
cd mainProject
python manage.py startapp userApp
```

## Project Structure
After setup, your project structure will look like:
```
virtualEnv/          # Virtual environment directory
mainProject/        # Main Django project
    ├── mainProject/ # Project configuration
    ├── userApp/     # Your user application
    └── manage.py   # Django management script
```

## Next Steps
1. Add 'userApp' to INSTALLED_APPS in mainProject/settings.py
2. Configure your database settings in settings.py
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Start development server: `python manage.py runserver`

## Notes
- Make sure your requirements.txt file exists with all required packages before installation
- On Windows, use `activate` instead of `source activate`
- For deactivating the virtual environment, simply run `deactivate`