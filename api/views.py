from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from api.serializers import RestaurantSerializer

 
@api_view(['POST'])
def register_restaurant(request):
    '''Restaurant register'''

    # Get data from request
    restaurant_data = request.data

    # Create new restaurant instance using serializer
    restaurant_serializer = RestaurantSerializer(data=restaurant_data)
    if restaurant_serializer.is_valid():
        restaurant_serializer.save()
        return Response({
            "restaurant": restaurant_serializer.data, 
            "msg": "Restaurant created successfully"
            }, status=status.HTTP_201_CREATED)
    else:
        return Response(restaurant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

