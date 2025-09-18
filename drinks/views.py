from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drinklist(request):
    # Logic to list drinks
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse(serializer.data, safe=False)