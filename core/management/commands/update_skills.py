from django.core.management.base import BaseCommand
from projects.models import Skill

class Command(BaseCommand):
    help = 'Update skills according to new specifications'

    def handle(self, *args, **options):
        self.stdout.write('Updating skills...')
        
        # Remove old skills
        skills_to_remove = ['React', 'MongoDB', 'TensorFlow', 'Git', 'Docker']
        for skill_name in skills_to_remove:
            try:
                skill = Skill.objects.get(name=skill_name)
                skill.delete()
                self.stdout.write(f'Removed skill: {skill_name}')
            except Skill.DoesNotExist:
                pass
        
        # Update database skills
        Skill.objects.filter(name='PostgreSQL').delete()
        
        # Add new database skills
        database_skills = [
            {'name': 'SQL/Oracle', 'category': 'database', 'proficiency': 85},
            {'name': 'SQLite3', 'category': 'database', 'proficiency': 55},
        ]
        
        for skill_data in database_skills:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults={
                    'category': skill_data['category'],
                    'proficiency': skill_data['proficiency']
                }
            )
            if created:
                self.stdout.write(f'Created skill: {skill.name}')
        
        # Add new tools
        tools_skills = [
            {'name': 'VSCode', 'category': 'tools', 'proficiency': 90},
            {'name': 'Git', 'category': 'tools', 'proficiency': 85},
        ]
        
        for skill_data in tools_skills:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults={
                    'category': skill_data['category'],
                    'proficiency': skill_data['proficiency']
                }
            )
            if created:
                self.stdout.write(f'Created skill: {skill.name}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully updated skills!')
        )
