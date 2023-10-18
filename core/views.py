from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, ProjectField, Project
from django.views.generic import DetailView
from .forms import ContactForm


# Create your views here.
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project_detail.html', {'project': project})

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

def contact_me(requests):
    if requests.method == 'POST':
        form = ContactForm(requests.POST)
        if form.is_valid():
            # Here you can save the message to the database or send an email.
            # For this example, we'll just print it to the console.
            print(f"Message from {form.cleaned_data['name']} ({form.cleaned_data['email']}): {form.cleaned_data['message']}")
            return redirect('home')  # Redirect to the homepage after submitting. Adjust as needed.
    else:
        form = ContactForm()
    return render(requests, 'contact_me.html', {'form': form})
