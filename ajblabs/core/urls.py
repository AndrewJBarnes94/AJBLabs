from django.urls import path
from . import views

app_name = 'core'  # Define the app's namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('/about', views.about, name='about'),
    path('/contact', views.contact, name='contact'),
]
