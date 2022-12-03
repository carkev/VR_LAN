"""AI is creating summary for ...
"""
from django.views.generic import TemplateView


# Create your views here.
class IndexViewPage(TemplateView):
    """Index Page view class.

    :parent: TemplateView
    """
    template_name = 'index.html'


class AboutPageView(TemplateView):
    """About page view class.

    :parent: TemplateView
    """
    template_name = "about.html"
