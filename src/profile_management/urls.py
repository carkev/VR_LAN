# accounts/urls.py
"""Accounts app router.
"""
from django.urls import path

from .views import ProfilManagementView, ProfilManagementUpdate, ProfilManagementDelete

urlpatterns = [
    path('my-profile/<int:pk>/', ProfilManagementView.as_view(), name="users_profile"),
    path('update_profile/<int:pk>/', ProfilManagementUpdate.as_view(), name="user_update"),
    path('delete_profile/<int:pk>/', ProfilManagementDelete.as_view(), name="user_delete"),


    
]
