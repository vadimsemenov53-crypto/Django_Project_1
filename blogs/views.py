from django.shortcuts import render
from blogs.models import BlogPost
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

# Create your views here.

class BlogListView(ListView):
    model = BlogPost


class BlogCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'image',)
    success_url = reverse_lazy('blogs:blog_list')
