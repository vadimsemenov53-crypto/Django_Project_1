from django.shortcuts import render
from blogs.models import BlogPost
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

# Create your views here.

class BlogListView(ListView):
    model = BlogPost
    template_name = 'base_blog.html'
