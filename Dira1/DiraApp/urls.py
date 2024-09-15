from django.urls import path
from . import views
from .views import register, login_view 

urlpatterns = [
    path('', views.home_dira, name='home_dira'),  # Home page
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
]
