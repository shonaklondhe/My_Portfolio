from django.core.management.base import BaseCommand
from projects.models import Project

class Command(BaseCommand):
    help = 'Fix ML Price Predictor GitHub link'

    def handle(self, *args, **options):
        self.stdout.write('Fixing ML Price Predictor GitHub link...')
        
        # Update ML Price Predictor project link
        try:
            project = Project.objects.get(title='ML Price Predictor')
            project.github_url = 'https://github.com/shonaklondhe/ML-Price-Predictor'
            project.save()
            self.stdout.write(f'Updated ML Price Predictor GitHub URL to: {project.github_url}')
        except Project.DoesNotExist:
            self.stdout.write('ML Price Predictor project not found')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully updated ML Price Predictor GitHub link!')
        )
