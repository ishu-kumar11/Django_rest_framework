from django.urls import path
from .views import deserialize_demo

urlpatterns = [
    path('', deserialize_demo),
]