from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import Post
# Create your views here.

posts = [
    { #Dummy Post 1
        'author': 'Nkozy',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    { #Dummy Post 2
        'author': 'Theo Katzman',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, template_name='blog/home.html', context=context)

def about(request):
    return render(request, template_name='blog/about.html', context={'title':'About'})

def logout_view(request):
    logout(request)