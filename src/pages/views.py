"""AI is creating summary for ...
"""
from django.views.generic import TemplateView
from .models import Staff
from django.views.generic import ListView


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
