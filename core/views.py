from django.shortcuts import render
from django.views.generic import TemplateView
from projects.models import Project, Skill
from blog.models import BlogPost

class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_projects'] = Project.objects.filter(featured=True)[:3]
        context['recent_posts'] = BlogPost.objects.filter(status='published')[:3]
        context['skills'] = Skill.objects.all()
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        return context

class ResumeView(TemplateView):
    template_name = 'core/resume.html'
