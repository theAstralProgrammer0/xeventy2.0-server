# Xeventy2.0 Django Backend

This documentation lists out clear instructions on how to setup and run the
backend of the xeventy2.0 health limited website.

## Setup

I utilized an end-to-end approach by creating a Django <app> that exposes a
REST API for my stored (article, news, or blog) objects. This API is built
with Django REST Framework (DRF), and for the blog data—a large
dataset—includes HATEOAS-style pagination (by returning next/previous links),
and leverages Redis caching to avoid repeated PostgreSQL queries. I then had
my Next.js front end fetch the dynamic data in form of each objects'
attributes corresponding to the Next.js components' props.

### Project Structure
```
xeventy2.0-server/
├── README.md 
├── db.sqlite3 
├── manage.py
├── requirements.txt     # List of required libraries for backend functionality 
├── env/                 # virtual environment directory 
├── x2h/
│   ├── __init__.py
│   ├── settings.py      # (modified to add caching, REST Framework, and blog app)
│   ├── urls.py          # (modified to include blog URLs)
│   └── wsgi.py
├── blog/                # blog Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── pagination.py   # custom pagination class for HATEOAS links
│
├── news/               # news Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
└── static/                # static files for Django admin page styling
```
