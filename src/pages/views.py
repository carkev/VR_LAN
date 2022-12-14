"""AI is creating summary for ...
"""
from django.views.generic import TemplateView, ListView

from .models import Staff


# Create your views here.
class IndexViewPage(TemplateView):
    """Index Page view class.

    :parent: TemplateView
    """
    template_name = 'index.html'


class AboutPageView(ListView):
    """About page view class.

    :parent: TemplateView
    """
    model = Staff
    template_name = "about.html"
