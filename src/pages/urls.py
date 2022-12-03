# pages/urls.py
"""URL routing module.
"""
from django.urls import path

from .views import IndexViewPage, AboutPageView


urlpatterns = [
    path('', IndexViewPage.as_view(), name='index'),
    path("about/", AboutPageView.as_view(), name="about")
]
