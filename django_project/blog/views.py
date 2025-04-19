from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import Post
# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, template_name='blog/home.html', context=context)

class PostListView(ListView):
    # These are just parameters for ListView
    # What model to use in each post
    model = Post
    # What template to use
    template_name = 'blog/home.html'
    # What is the name the context
    context_object_name = 'posts' 
    # Set order of posts to be most recent first
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    # A view with a form to create a new post
    model = Post
    # Set fields for form
    fields = ['title', 'content']
    
    # Tells Django to use the current user who's sending the request as the a
    # author of the form.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # A view with a form to create a new post
    model = Post
    # Set fields for form
    fields = ['title', 'content']
    
    # Tells Django to use the current user who's sending the request as the a
    # author of the form.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def about(request):
    return render(request, template_name='blog/about.html', context={'title':'About'})

def logout_view(request):
    logout(request)

