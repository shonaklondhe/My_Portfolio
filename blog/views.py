from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    queryset = BlogPost.objects.filter(status='published')
    paginate_by = 6

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    queryset = BlogPost.objects.filter(status='published')
