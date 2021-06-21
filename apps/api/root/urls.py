

from django.urls import path
from .views import APIRoot

urlpatterns = [
    path('', APIRoot.as_view(), name="API Index")
]
