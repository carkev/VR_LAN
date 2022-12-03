# accounts/tests.py
"""Module to test accounts views.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignupPageView


# Create your tests here.
class CustomUserTests(TestCase):
    """CustomUser test class.

    :parent: TestCase
    """
    def test_create_user(self) -> None:
        """Method which test the user creation method.

        :return: Test create_user method.
        :rtype: None
        """
        User = get_user_model()
        user = User.objects.create_user(
            username="jdoe", email="jdoe@mail.com", password="testpass123"
        )
        self.assertEqual(user.username, 'jdoe')
        self.assertEqual(user.email, 'jdoe@mail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Method which test the user creation method.

        :return: Test create_user method.
        :rtype: None
        """
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin",
            email="superadmin@mail.com",
            password="testpass123"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@mail.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):
    """SignupPage test class.

    :parent: TestCase
    """
    username = "newuser"
    email = "newuser@email.com"

    def setUp(self) -> None:
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        """Method to test signup template.

        :return: Test signup template method.
        :rtype: None
        """
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, 'toto')

    def test_signup_form(self):
        """Method to test signup form.

        :return: Test signup form method.
        :rtype: None
        """
        new_user = get_user_model().objects.create_user(self.username,
                                                        self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username,
                         self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        """Method to test signup view.

        :return: Test signup views method.
        :rtype: None
        """
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
