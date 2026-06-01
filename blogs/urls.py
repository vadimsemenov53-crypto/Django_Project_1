from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import BlogListView, BlogCreateView

app_name = BlogsConfig.name

urlpatterns = [
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_list/create', BlogCreateView.as_view(), name='blog_create'),
]