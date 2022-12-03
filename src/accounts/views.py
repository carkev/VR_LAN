# accounts/views.py
"""Accounts app views.
"""
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


# Create your views here.
class SignupPageView(generic.CreateView):
    """Signup view custom class.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
