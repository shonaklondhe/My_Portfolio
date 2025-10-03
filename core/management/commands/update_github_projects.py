from django.core.management.base import BaseCommand
from projects.models import Project, Tag

class Command(BaseCommand):
    help = 'Update projects with detailed GitHub repository information'

    def handle(self, *args, **options):
        self.stdout.write('Updating GitHub projects with detailed information...')
        
        # Update Crop Fertilizer Prediction project
        try:
            project = Project.objects.get(title='Crop Fertilizer Prediction')
            project.description = '''A comprehensive machine learning application that predicts the most suitable fertilizer for crops based on soil and environmental parameters. Built with Django framework and advanced ML algorithms.

## Key Features:
- **Intelligent Prediction**: Uses machine learning models to recommend optimal fertilizers
- **Multi-parameter Analysis**: Considers soil NPK levels, pH, temperature, humidity, and rainfall
- **Django Web Interface**: User-friendly web application with responsive design
- **Model Persistence**: Trained models saved using joblib for fast predictions
- **Real-time Results**: Instant fertilizer recommendations with confidence scores

## Technologies Used:
- **Backend**: Django, Python
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Frontend**: HTML5, CSS3, Bootstrap
- **Database**: SQLite3
- **Model Storage**: Joblib for model serialization

## Project Structure:
- **app/**: Main Django application with ML logic
- **savedModels/**: Trained machine learning models
- **templates/**: HTML templates for web interface
- **static/**: CSS, JavaScript, and image assets
- **crop_fertilizer_prediction/**: Django project configuration

## Impact:
This project helps farmers make data-driven decisions about fertilizer usage, potentially improving crop yield while optimizing resource utilization. The ML model analyzes multiple soil and weather parameters to provide accurate fertilizer recommendations.'''
            
            project.short_description = 'ML-powered fertilizer recommendation system for optimal crop yield using soil and weather data analysis'
            project.github_url = 'https://github.com/shonaklondhe/Crop-Fertilizer-Prediction'
            project.save()
            
            # Clear existing tags and add new ones
            project.tags.clear()
            tag_names = ['Python', 'Django', 'Machine Learning', 'HTML/CSS']
            for tag_name in tag_names:
                try:
                    tag = Tag.objects.get(name=tag_name)
                    project.tags.add(tag)
                except Tag.DoesNotExist:
                    pass
            
            self.stdout.write(f'Updated project: {project.title}')
            
        except Project.DoesNotExist:
            self.stdout.write('Crop Fertilizer Prediction project not found')
        
        # Update Weather Prediction project
        try:
            project = Project.objects.get(title='Weather Prediction System')
            project.description = '''An advanced weather forecasting system that leverages machine learning algorithms to predict weather conditions with high accuracy. Built using Python and modern ML techniques for reliable weather predictions.

## Key Features:
- **Multi-parameter Forecasting**: Predicts temperature, humidity, precipitation, and weather patterns
- **Historical Data Analysis**: Uses extensive historical weather data for training
- **Machine Learning Models**: Implements various algorithms for optimal prediction accuracy
- **Interactive Visualizations**: Charts and graphs for weather trend analysis
- **API Integration**: Real-time weather data integration capabilities
- **Responsive Interface**: Clean, modern web interface for easy access

## Technologies Used:
- **Machine Learning**: Scikit-learn, TensorFlow/Keras
- **Data Processing**: Pandas, NumPy, Matplotlib, Seaborn
- **Backend**: Python, Flask/Django
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Visualization**: Plotly, Chart.js
- **APIs**: Weather data APIs for real-time information

## Machine Learning Approach:
- **Data Preprocessing**: Feature engineering and data cleaning
- **Model Selection**: Comparison of Linear Regression, Random Forest, and Neural Networks
- **Feature Analysis**: Temperature, humidity, pressure, wind patterns
- **Prediction Accuracy**: Optimized models for reliable forecasting
- **Time Series Analysis**: Temporal pattern recognition for weather trends

## Applications:
- Agricultural planning and crop management
- Event planning and outdoor activities
- Transportation and logistics optimization
- Emergency preparedness and disaster management
- Personal weather planning and alerts'''
            
            project.short_description = 'Advanced ML-based weather forecasting system with multi-parameter prediction and interactive visualizations'
            project.github_url = 'https://github.com/shonaklondhe/Weather-Prediction'
            project.save()
            
            # Clear existing tags and add new ones
            project.tags.clear()
            tag_names = ['Python', 'Machine Learning', 'JavaScript']
            for tag_name in tag_names:
                try:
                    tag = Tag.objects.get(name=tag_name)
                    project.tags.add(tag)
                except Tag.DoesNotExist:
                    pass
            
            self.stdout.write(f'Updated project: {project.title}')
            
        except Project.DoesNotExist:
            self.stdout.write('Weather Prediction System project not found')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully updated GitHub projects with detailed information!')
        )
