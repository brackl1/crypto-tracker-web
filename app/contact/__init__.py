# app/contact/__init__.py

from flask import Blueprint

contact = Blueprint('contact', __name__)

from . import views
