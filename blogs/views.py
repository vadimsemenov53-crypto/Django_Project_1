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


class BlogDetailView(DetailView):
    model = BlogPost
    success_url = reverse_lazy('blogs:blog_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'image',)
    success_url = reverse_lazy('blogs:blog_list')

    def get_success_url(self):
        return reverse('blogs:blog_detail', args=[self.kwargs.get('pk')])
