"""
URL configuration for AJBLabs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('resume/', views.resume, name='resume'),
    path('about-me/', views.about_me, name='about_me'),
    path('ambitions/', views.ambitions, name='ambitions'),
    path('contact_me/', views.contact_me, name='contact_me'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]
