from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

class MLDemoView(TemplateView):
    template_name = 'ml_demos/demo.html'

@method_decorator(csrf_exempt, name='dispatch')
class PredictView(TemplateView):
    def post(self, request):
        try:
            # Indian real estate price prediction
            data = json.loads(request.body)
            bedrooms = float(data.get('bedrooms', 2))
            kitchen = float(data.get('kitchen', 1))
            hall = float(data.get('hall', 1))
            sqft = float(data.get('sqft', 800))
            city = data.get('city', 'pune')
            
            # City multipliers for Indian real estate
            city_multipliers = {
                'mumbai': 1.8,
                'delhi': 1.6,
                'bangalore': 1.4,
                'pune': 1.2,
                'hyderabad': 1.1,
                'chennai': 1.1,
                'kolkata': 0.9,
                'ahmedabad': 0.8,
                'other': 0.7
            }
            
            city_multiplier = city_multipliers.get(city.lower(), 0.7)
            
            # Base price calculation (in INR)
            base_price = (
                (bedrooms * 800000) +      # ₹8 lakh per bedroom
                (kitchen * 400000) +       # ₹4 lakh per kitchen
                (hall * 600000) +          # ₹6 lakh per hall
                (sqft * 4000)              # ₹4000 per sqft
            )
            
            # Apply city multiplier
            final_price = base_price * city_multiplier
            
            # Add some randomness for realism
            import random
            variation = random.uniform(0.9, 1.1)
            final_price *= variation
            
            return JsonResponse({
                'success': True,
                'prediction': round(final_price, 0),
                'message': f'Estimated property price: ₹{final_price:,.0f}',
                'details': {
                    'city': city.title(),
                    'bedrooms': int(bedrooms),
                    'kitchen': int(kitchen),
                    'hall': int(hall),
                    'sqft': int(sqft),
                    'price_per_sqft': round(final_price / sqft, 0)
                }
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
