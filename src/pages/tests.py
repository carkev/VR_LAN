"""Test templates, views and forms from Pages package module.
"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import IndexViewPage, AboutPageView


# Create your tests here.
class IndexPageTests(SimpleTestCase):
    """IndexPage test class.

    :parent: SimpleTestCase
    """

    def setUp(self) -> None:
        url = reverse("index")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        """Method to test the url.

        :return: Test the url.
        :rtype: None
        """
        self.assertEqual(self.response.status_code, 200)

    def test_index_template(self):
        """Method to test the template.

        :return: Test the template.
        :rtype: None
        """
        self.assertTemplateUsed(self.response, "index.html")

    def test_index_contains_correct_html(self):
        """Method to test the html content.

        :return: Test the html content.
        :rtype: None
        """
        self.assertContains(self.response, "Home page.")

    def test_index_does_not_contains_incorrect_html(self):
        """Method to test the html content.

        :return: Test the html content.
        :rtype: None
        """
        self.assertNotContains(self.response, "toto")

    def test_index_url_resolves_indexpageview(self):
        """Method to test the template name.

        :return: Test the template name.
        :rtype: None
        """
        view = resolve("/")
        self.assertEqual(view.func.__name__, IndexViewPage.as_view().__name__)


class AboutPageTests(SimpleTestCase):
    """About page test.
    """
    def setUp(self) -> None:
        url = reverse("about")
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        """Method to test aboutpage status code.

        :return: Test aboutpage status code.
        :rtype: None
        """
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        """Method to test aboutpage template.

        :return: Test aboutpage template.
        :rtype: None
        """
        self.assertTemplateUsed(self.response, "about.html")

    def test_aboutpage_contains_correct_html(self):
        """Method to test aboutpage content.

        :return: Test aboutpage content.
        :rtype: None
        """
        self.assertContains(self.response, "About Page")

    def test_aboutpage_does_not_contain_incorrect_html(self):
        """Method to test aboutpage content.

        :return: Test aboutpage content.
        :rtype: None
        """
        self.assertNotContains(self.response, "toto")

    def test_aboutpage_url_resolves_aboutpageview(self):
        """Method to test aboutpage name.

        :return: Test aboutpage name.
        :rtype: None
        """
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
