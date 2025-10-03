from django.core.management.base import BaseCommand
from projects.models import Project, Tag

class Command(BaseCommand):
    help = 'Update projects with real GitHub repository links'

    def handle(self, *args, **options):
        self.stdout.write('Updating projects with real GitHub links...')
        
        # Update Weather Prediction project
        try:
            project = Project.objects.get(title='Weather Prediction System')
            project.github_url = 'https://github.com/shonaklondhe/Weather-Prediction'
            project.save()
            self.stdout.write(f'Updated Weather Prediction GitHub URL')
        except Project.DoesNotExist:
            self.stdout.write('Weather Prediction project not found')
        
        # Update Crop Fertilizer Prediction project
        try:
            project = Project.objects.get(title='Crop Fertilizer Prediction')
            project.github_url = 'https://github.com/shonaklondhe/Crop-Fertilizer-Prediction'
            project.save()
            self.stdout.write(f'Updated Crop Fertilizer Prediction GitHub URL')
        except Project.DoesNotExist:
            self.stdout.write('Crop Fertilizer Prediction project not found')
        
        # Update Portfolio Website project
        try:
            project = Project.objects.get(title='Portfolio Website')
            project.github_url = 'https://github.com/shonaklondhe/My_Portfolio'
            project.save()
            self.stdout.write(f'Updated Portfolio Website GitHub URL')
        except Project.DoesNotExist:
            self.stdout.write('Portfolio Website project not found')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully updated all GitHub repository links!')
        )
