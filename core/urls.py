from django.urls import path

from core.views import aPage

urlpatterns = [
    path('a/', aPage),
]
