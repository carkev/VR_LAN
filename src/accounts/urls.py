# accounts/urls.py
"""Accounts app router.
"""
from django.urls import path

from .views import SignupPageView, ProfilManagementView

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
]
