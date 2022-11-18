#!/bin/bash
python -m pip install Django
django-admin startproject ${PROJECT_NAME} .
pip install djangorestframework
pip freeze > requirements.txt