from django.db import models
import json

class MLPrediction(models.Model):
    input_data = models.JSONField()
    prediction = models.JSONField()
    model_name = models.CharField(max_length=100, default='house_price_predictor')
    confidence = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.model_name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    class Meta:
        ordering = ['-created_at']
