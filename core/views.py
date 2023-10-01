from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, ProjectField, Project

# Create your views here.
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project_detail.html', {'project': project})


def home(requests):
    return render(requests, 'home.html', {})

def blog(request, pk=None):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def resume(requests):
    return render(requests, "resume.html", {})

def about_me(requests):
    return render(requests, "about_me.html", {})

def ambitions(requests):
    return render(requests, 'ambitions.html', {})

def contact_me(requests):
    return render(requests, 'contact_me.html', {})