from django.contrib import admin
from .models import MLPrediction

@admin.register(MLPrediction)
class MLPredictionAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'created_at', 'confidence']
    list_filter = ['model_name', 'created_at']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
