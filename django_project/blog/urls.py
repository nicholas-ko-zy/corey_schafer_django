from django.urls import path
from . import views

urlpatterns = [
    # Empty path - Home page
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
