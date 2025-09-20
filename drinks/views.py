from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drinklist(request):
    # Logic to list drinks
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse(serializer.data, safe=False)

def normalize_name(request, name):
    """
    Normalize a given name.
    For now, this function simply passes through the name as requested.
    """
    try:
        # Basic validation - ensure name is not empty
        if not name or not name.strip():
            return JsonResponse({
                'error': 'Name cannot be empty'
            }, status=400)
        
        # For now, just return the name as-is (pass through)
        normalized_name = name.strip()
        
        return JsonResponse({
            'original_name': name,
            'normalized_name': normalized_name
        })
        
    except Exception as e:
        return JsonResponse({
            'error': 'An error occurred while normalizing the name'
        }, status=500)