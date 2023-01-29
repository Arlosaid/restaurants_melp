from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Restaurants

from .serializers import DeleteRestaurantSerializer,  RestaurantSerializer


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
    restaurant_exists = Restaurants.objects.filter(id=id_restaurant).exists()
    if restaurant_exists:
        restaurant = Restaurants.objects.filter(id=id_restaurant)
        restaurant_serializer = RestaurantSerializer(restaurant, many=True)
        return Response({
            "Restaurant": restaurant_serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            "error": "No restaurant was found with the specified id."
        },status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_restaurant(request, id):
    restaurant = get_object_or_404(Restaurants, id=id)
    serializer = RestaurantSerializer(restaurant, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_restaurant(request, id):
    serializer = DeleteRestaurantSerializer(data={'id': id})
    if serializer.is_valid():
        serializer.delete()
        return Response({"message": "The restaurant was successfully deleted."}, status=status.HTTP_200_OK)
    else:
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
