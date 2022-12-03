"""Module which customize the admin pannel connexion.

Now, only staff members can connect there.
"""
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# from django.contrib.admin.views.decorators import staff_member_required

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    """Class to customize UserAdmin class.

    :parent: UserAdmin
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "is_superuser", ]

admin.site.register(CustomUser, CustomUserAdmin)
# Ensure users go through the allauth workflow when logging into admin.
# admin.site.login = staff_member_required(
#     admin.site.login, login_url='/accounts/login')
# Run the standard admin set-up.
# admin.autodiscover()
