from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, ProjectField, Project
from django.views.generic import DetailView
from .forms import ContactForm
import requests
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def project_fields(request, field):
    project_field = ProjectField.objects.get(field=field)

    projects = Project.objects.filter(project_field=project_field)

    return render(request, 'project_fields.html', {'projects': projects, 'project_field': project_field})


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    code_content = requests.get(project.code_download_url).text
    context = {
        'project': project,
        'code_content': code_content,
    }

    return render(request, 'project_detail.html', {'context': context})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'  # <app>/<model>_<viewtype>.html by default
    context_object_name = 'post'

def home(requests):
    return render(requests, 'home.html', {})

def articles(request, pk=None):
    posts = Post.objects.all()
    return render(request, 'articles.html', {'posts': posts})

def resume(requests):
    return render(requests, "resume.html", {})

def about_me(requests):
    return render(requests, "about_me.html", {})

def contact_me(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            recipient_list = ['ajbarnes@ajblabs.com']

            send_mail(subject, message, from_email, recipient_list)
            
            messages.success(request, 'Thank you for your message. We will get back to you shortly.')
            return redirect('contact_page')  # Redirect back to contact page after sending email
    else:
        form = ContactForm()
    return render(request, 'contact_me.html', {'form': form})
