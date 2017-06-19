# my-test-flaskr
A test sample for personal study purpose.

Folder Structure:

    ├── README.md
    ├── app
    │   ├── __init__.py
    │   ├── dashboard
    │   │   ├── __init__.py
    │   │   ├── errors.py
    │   │   ├── form.py
    │   │   └── view.py
    │   ├── models.py
    │   ├── pages
    │   │   ├── __init__.py
    │   │   ├── errors.py
    │   │   ├── form.py
    │   │   └── view.py
    │   ├── static
    │   └── template
    │       ├── dashboard
    │       ├── home
    │       ├── layout.html
    │       └── pages
    ├── config.py
    ├── setup.py
    └── tests

Consider making any .py file (except __init__.py) under views folder a blueprint, and load and register the blueprints in app/__init__.py file.

The all blueprints will share one layout of template/layout.html.

The all blueprints share the same static source.