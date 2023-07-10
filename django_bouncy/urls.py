"""URLs for the Django-Bouncy App"""
from django.urls import re_path
# pylint: disable=invalid-name
from django_bouncy.views import endpoint

urlpatterns = [
    re_path(r'^$', endpoint)
]
