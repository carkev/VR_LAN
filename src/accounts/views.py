# accounts/views.py
"""Accounts app views.
"""
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render 

from .forms import CustomUserCreationForm,EditProfileForm


# Create your views here.
class SignupPageView(generic.CreateView):
    """Signup view custom class.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class ProfilManagementView(generic.TemplateView):
    """...
    """
    form_class = EditProfileForm
    #success_url = reverse_lazy("profilManagement")
    template_name = "profilManagement.html"

@login_required
def user_profil(request):
    return render(request, 'profilManagement.html')

