from django.core.management.base import BaseCommand
from projects.models import Project, Tag, Skill
from blog.models import BlogPost

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create Tags
        tags_data = [
            {'name': 'Python', 'color': '#3776ab'},
            {'name': 'Django', 'color': '#092e20'},
            {'name': 'JavaScript', 'color': '#f7df1e'},
            {'name': 'React', 'color': '#61dafb'},
            {'name': 'Machine Learning', 'color': '#ff6b6b'},
            {'name': 'HTML/CSS', 'color': '#e34f26'},
            {'name': 'PostgreSQL', 'color': '#336791'},
            {'name': 'Docker', 'color': '#2496ed'},
        ]
        
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(
                name=tag_data['name'],
                defaults={'color': tag_data['color']}
            )
            if created:
                self.stdout.write(f'Created tag: {tag.name}')

        # Create Skills
        skills_data = [
            {'name': 'Python', 'category': 'backend', 'proficiency': 90},
            {'name': 'Django', 'category': 'backend', 'proficiency': 85},
            {'name': 'JavaScript', 'category': 'frontend', 'proficiency': 80},
            {'name': 'React', 'category': 'frontend', 'proficiency': 75},
            {'name': 'HTML/CSS', 'category': 'frontend', 'proficiency': 90},
            {'name': 'PostgreSQL', 'category': 'database', 'proficiency': 70},
            {'name': 'MongoDB', 'category': 'database', 'proficiency': 65},
            {'name': 'Scikit-learn', 'category': 'ml', 'proficiency': 80},
            {'name': 'TensorFlow', 'category': 'ml', 'proficiency': 70},
            {'name': 'Git', 'category': 'tools', 'proficiency': 85},
            {'name': 'Docker', 'category': 'tools', 'proficiency': 70},
        ]
        
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults={
                    'category': skill_data['category'],
                    'proficiency': skill_data['proficiency']
                }
            )
            if created:
                self.stdout.write(f'Created skill: {skill.name}')

        # Create Projects
        projects_data = [
            {
                'title': 'E-commerce Platform',
                'short_description': 'Full-stack e-commerce solution with Django and React',
                'description': 'A complete e-commerce platform built with Django REST API backend and React frontend. Features include user authentication, product catalog, shopping cart, payment integration, and admin dashboard.',
                'github_url': 'https://github.com/shonaklondhe/ecommerce-platform',
                'featured': True,
                'tags': ['Python', 'Django', 'React', 'PostgreSQL']
            },
            {
                'title': 'ML Price Predictor',
                'short_description': 'Machine learning model for real estate price prediction',
                'description': 'A machine learning application that predicts real estate prices based on various features like location, size, and amenities. Built using scikit-learn and deployed with Django.',
                'github_url': 'https://github.com/shonaklondhe/ml-price-predictor',
                'featured': True,
                'tags': ['Python', 'Machine Learning', 'Django']
            },
            {
                'title': 'Task Management App',
                'short_description': 'Collaborative task management with real-time updates',
                'description': 'A collaborative task management application with real-time updates, user roles, and project organization. Features drag-and-drop interface and team collaboration tools.',
                'github_url': 'https://github.com/shonaklondhe/task-manager',
                'featured': False,
                'tags': ['JavaScript', 'React', 'Django']
            },
            {
                'title': 'Portfolio Website',
                'short_description': 'Personal portfolio with ML demo and blog',
                'description': 'A responsive portfolio website showcasing projects, skills, and blog posts. Includes an interactive ML demo for real estate price prediction.',
                'github_url': 'https://github.com/shonaklondhe/portfolio',
                'featured': True,
                'tags': ['Python', 'Django', 'HTML/CSS', 'Machine Learning']
            }
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults={
                    'short_description': project_data['short_description'],
                    'description': project_data['description'],
                    'github_url': project_data['github_url'],
                    'featured': project_data['featured']
                }
            )
            if created:
                # Add tags
                for tag_name in project_data['tags']:
                    tag = Tag.objects.get(name=tag_name)
                    project.tags.add(tag)
                self.stdout.write(f'Created project: {project.title}')

        # Create Blog Posts
        blog_posts_data = [
            {
                'title': 'Getting Started with Django',
                'content': '''Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. In this post, we'll explore the basics of Django and build a simple web application.

## Why Django?

Django follows the "batteries included" philosophy, providing many built-in features:
- Admin interface
- ORM (Object-Relational Mapping)
- Authentication system
- URL routing
- Template engine

## Setting Up Your First Django Project

1. Install Django: `pip install django`
2. Create project: `django-admin startproject myproject`
3. Run server: `python manage.py runserver`

Django makes web development fast and enjoyable!''',
                'status': 'published',
                'featured': True,
                'read_time': 5,
                'tags': ['Python', 'Django']
            },
            {
                'title': 'Machine Learning in Web Applications',
                'content': '''Integrating machine learning models into web applications opens up exciting possibilities. Here's how to deploy ML models using Django.

## Key Considerations

- Model serialization with joblib or pickle
- API design for predictions
- Handling model updates
- Performance optimization

## Example Implementation

```python
import joblib
from django.http import JsonResponse

def predict_view(request):
    model = joblib.load('model.pkl')
    prediction = model.predict(data)
    return JsonResponse({'prediction': prediction})
```

This approach makes ML accessible through web interfaces.''',
                'status': 'published',
                'featured': False,
                'read_time': 7,
                'tags': ['Machine Learning', 'Python', 'Django']
            },
            {
                'title': 'Building Responsive Web Interfaces',
                'content': '''Creating responsive web interfaces is crucial in today's multi-device world. Here are best practices for building adaptive layouts.

## CSS Grid and Flexbox

Modern CSS layout methods provide powerful tools:
- CSS Grid for 2D layouts
- Flexbox for 1D layouts
- Media queries for breakpoints

## Mobile-First Approach

Start with mobile design and progressively enhance:
1. Design for smallest screen first
2. Add complexity for larger screens
3. Test across devices

Responsive design ensures great user experience everywhere.''',
                'status': 'published',
                'featured': True,
                'read_time': 6,
                'tags': ['HTML/CSS', 'JavaScript']
            }
        ]
        
        for post_data in blog_posts_data:
            post, created = BlogPost.objects.get_or_create(
                title=post_data['title'],
                defaults={
                    'content': post_data['content'],
                    'status': post_data['status'],
                    'featured': post_data['featured'],
                    'read_time': post_data['read_time']
                }
            )
            if created:
                # Add tags
                for tag_name in post_data['tags']:
                    tag = Tag.objects.get(name=tag_name)
                    post.tags.add(tag)
                self.stdout.write(f'Created blog post: {post.title}')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data!')
        )
