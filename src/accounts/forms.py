# accounts/forms.py
"""Module of account forms.
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    """Class which customize UserCreationForm form class.

    :parent: UserCreationForm
    """
    class Meta:
        """Change the class behaviour.
        """
        model = get_user_model()
        fields = ("email", "email", )


class CustomUserChangeForm(UserChangeForm):
    """Class which customize UserChangForm form class.

    :parent: UserChangeForm
    """
    class Meta:
        """Change the class behaviour.
        """
        model = get_user_model()
        fields = ('email', 'username', )

class EditProfileForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'password',
        )

