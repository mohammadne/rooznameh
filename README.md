# Rooznameh

> Rooznameh is a persian word meaning Blog 📝

The blog platform written in django which users can create blog posts. Each blog post can be edited or deleted by the user who created it. Also it has features like categories, tags, and comments which makes it a good starting point for leaning and working with django.

## TODOs

- deploy on kind
- monitoring (metrics, structured logging, tracing)
- concurency
- authentication

```bash
# skeleton the project
django-admin startproject rooznameh

# run the django server
py manage.py runserver

# add an app to the project
py manage.py startapp users

# create super user for admin panel
py manage.py createsuperuser

# create shell to intract with models and server
py manage.py shell

py manage.py makemigrations # generate the required migrations from models
py manage.py migrate # run the actual migrations to the database
```
