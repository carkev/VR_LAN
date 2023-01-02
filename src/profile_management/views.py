# accounts/views.py
"""Accounts app views.
"""
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render 
from django.contrib.auth import get_user_model

from .forms import UpdateProfile
from accounts.models import CustomUser

#class ProfilManagementView(generic.TemplateView):
  

    #form_class = EditProfileForm
    #
    # model = get_user_model()
    # form = UpdateProfile
    # if form.is_valid():
      #   form.save()
    # success_url = reverse_lazy("profilManagement")
    # template_name = "profil_management.html"


@login_required
def user_profil(request):
    return render(request, 'profil_management.html')


class ProfilManagementView(generic.DetailView):
    model = CustomUser
    template_name = "profil_management.html"
    context_object_name = "user"

class ProfilManagementUpdate(generic.UpdateView):
    model = CustomUser
    template_name = "profil_update.html"
    fields = ['username', 'email', 'password']

class ProfilManagementDelete(generic.DeleteView):
    model = CustomUser
    template_name = "profil_delete.html"

