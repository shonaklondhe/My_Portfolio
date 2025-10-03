from django.urls import path
from . import views

app_name = 'ml_demos'

urlpatterns = [
    path('', views.MLDemoView.as_view(), name='demo'),
    path('predict/', views.PredictView.as_view(), name='predict'),
]
