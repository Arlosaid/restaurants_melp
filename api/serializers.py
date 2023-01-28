from rest_framework import serializers

from api.models import Restaurants



class RestaurantSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Restaurants
        fields = ('id', 'rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lng')


    def create(self, validated_data):
        restaurant = Restaurants.objects.create(
            id = validated_data['id'],
            rating = validated_data['rating'],
            name = validated_data['name'],
            site = validated_data['site'],
            email = validated_data['email'],
            phone = validated_data['phone'],
            street = validated_data['street'],
            city = validated_data['city'],
            state = validated_data['state'],
            lat = validated_data['lat'],
            lng = validated_data['lng'],
            
        )
        return restaurant
    