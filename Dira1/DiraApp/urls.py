from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_dira, name='home_dira'),  # Home page
]
