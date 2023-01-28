from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.models import Restaurants

from api.serializers import GetRestaurantSerializer, RestaurantSerializer

 
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

@api_view(['GET'])
def get_restaurant(request,id_restaurant):
    '''Obtiene todas las plantas registradas'''
    restaurant_exists = Restaurants.objects.filter(id=id_restaurant).exists()
    if restaurant_exists:
        restaurant = Restaurants.objects.filter(id=id_restaurant)
        restaurant_serializer = GetRestaurantSerializer(restaurant, many=True)
        return Response({
            "Restaurant": restaurant_serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

          