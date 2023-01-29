import re
from rest_framework import serializers

from api.models import Restaurants

from uuid import UUID

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Restaurants
        fields = ('id', 'rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lng')
        extra_kwargs = {'id': {'required': False}}
    
    def validate_id(self, value):
        try:
            UUID(value, version=4)
        except ValueError:
            raise serializers.ValidationError("The id value must be a v4 UUID.")
        return value

    def validate_rating(self, value):
        if value < 1 or value > 4:
            raise serializers.ValidationError("The rating value must be between 1 and 4.")
        return value

    def validate_email(self, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise serializers.ValidationError("The email value must be a valid email address.")
        return value    
    
    def create(self, validated_data):
        existing_record = Restaurants.objects.filter(
            name=validated_data['name'],
            site=validated_data['site'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            street=validated_data['street'],
            city=validated_data['city'],
            state=validated_data['state'],
            lat=validated_data['lat'],
            lng=validated_data['lng'],
        ).first()
        if existing_record:
            raise serializers.ValidationError("A record with the same data already exists.")
        return Restaurants.objects.create(**validated_data)

    def get_restaurants(self, Restaurants):
        return {
            "restaurant_id": Restaurants.id,
            "restaurant_rating": Restaurants.rating,
            "restaurant_name": Restaurants.name,
            "restaurant_site": Restaurants.site,
            "restaurant_email": Restaurants.email,
            "restaurant_phone": Restaurants.phone,
            "restaurant_street": Restaurants.street,
            "restaurant_city": Restaurants.city,   
            "restaurant_state": Restaurants.state ,
            "restaurant_lat": Restaurants.lat, 
            "restaurant_lng": Restaurants.lng,
        }
    def update(self, instance, validated_data):
            restaurant = instance
            if restaurant:
                restaurant.rating = validated_data.get('rating', restaurant.rating)
                restaurant.name = validated_data.get('name', restaurant.name)
                restaurant.site = validated_data.get('site', restaurant.site)
                restaurant.email = validated_data.get('email', restaurant.email)
                restaurant.phone = validated_data.get('phone', restaurant.phone)
                restaurant.street = validated_data.get('street', restaurant.street)
                restaurant.city = validated_data.get('city', restaurant.city)
                restaurant.state = validated_data.get('state', restaurant.state)
                restaurant.lat = validated_data.get('lat', restaurant.lat)
                restaurant.lng = validated_data.get('lng', restaurant.lng)
                restaurant.save()
                return restaurant
            else:
                raise serializers.ValidationError("No restaurant was found with the specified id.")

class DeleteRestaurantSerializer(serializers.Serializer):
    id = serializers.CharField()
    
    def delete(self):
        restaurant = Restaurants.objects.filter(id=self.validated_data['id']).first()
        if restaurant:
            restaurant.delete()
        else:
            raise serializers.ValidationError("No restaurant was found with the specified id.")


        

    
