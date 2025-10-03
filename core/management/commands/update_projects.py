from django.core.management.base import BaseCommand
from projects.models import Project, Tag

class Command(BaseCommand):
    help = 'Update projects according to new specifications'

    def handle(self, *args, **options):
        self.stdout.write('Updating projects...')
        
        # Remove old projects
        projects_to_remove = ['Task Management App', 'E-commerce Platform']
        for project_title in projects_to_remove:
            try:
                project = Project.objects.get(title=project_title)
                project.delete()
                self.stdout.write(f'Removed project: {project_title}')
            except Project.DoesNotExist:
                pass
        
        # Add new projects
        new_projects = [
            {
                'title': 'Crop Fertilizer Prediction',
                'short_description': 'ML model to predict optimal fertilizer for crops based on soil conditions',
                'description': 'An intelligent agricultural solution that uses machine learning to predict the most suitable fertilizer for crops based on soil parameters like nitrogen, phosphorus, potassium levels, pH, and environmental conditions. Built with Python and scikit-learn.',
                'github_url': 'https://github.com/shonaklondhe/crop-fertilizer-prediction',
                'featured': True,
                'tags': ['Python', 'Machine Learning', 'Django']
            },
            {
                'title': 'Weather Prediction System',
                'short_description': 'Advanced weather forecasting using machine learning algorithms',
                'description': 'A comprehensive weather prediction system that uses historical weather data and machine learning algorithms to forecast weather conditions. Features include temperature, humidity, and precipitation predictions with interactive visualizations.',
                'github_url': 'https://github.com/shonaklondhe/weather-prediction',
                'featured': True,
                'tags': ['Python', 'Machine Learning', 'JavaScript']
            }
        ]
        
        for project_data in new_projects:
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
                    try:
                        tag = Tag.objects.get(name=tag_name)
                        project.tags.add(tag)
                    except Tag.DoesNotExist:
                        pass
                self.stdout.write(f'Created project: {project.title}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully updated projects!')
        )
