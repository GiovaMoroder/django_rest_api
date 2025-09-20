from django.http import JsonResponse
from rest_framework.exceptions import NotFound
from .models import Drink
from .serializers import DrinkSerializer
from .normalizers import NameNormalizer

def drinklist(request):
    # Logic to list drinks
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse(serializer.data, safe=False)

def normalize_name(request, name):
    """
    Normalize a given name using the NameNormalizer class.
    """
    if not name or not name.strip():
        return JsonResponse({'error': 'Name cannot be empty'}, status=400)

    normalizer = NameNormalizer()

    try:
        normalized_name = normalizer.normalize(name)
    except Exception:
        return JsonResponse({'error': 'Normalization failed'}, status=500)

    if normalized_name is None:
        raise NotFound(f"Name not found: {name}")

    return JsonResponse({
        'original_name': name,
        'normalized_name': normalized_name
    })
