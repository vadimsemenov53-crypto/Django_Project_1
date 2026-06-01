from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import BlogListView

app_name = BlogsConfig.name

urlpatterns = [
    path('blog_list', BlogListView.as_view(), name='blog_list'),
]