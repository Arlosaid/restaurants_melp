from rest_framework import serializers

from api.models import Restaurants



class RestaurantSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Restaurants
        fields = ('id', 'rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lng')

    # def create(self, validated_data):
    #     restaurant = Restaurants.objects.create(
    #         id = validated_data['id'],
    #         rating = validated_data['rating'],
    #         name = validated_data['name'],
    #         site = validated_data['site'],
    #         email = validated_data['email'],
    #         phone = validated_data['phone'],
    #         street = validated_data['street'],
    #         city = validated_data['city'],
    #         state = validated_data['state'],
    #         lat = validated_data['lat'],
    #         lng = validated_data['lng'],   
    #     )
    #     return restaurant
    def create(self,validated_data):
        return Restaurants.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.rating = validated_data.get('rating', instance.rating)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.site = validated_data.get('site', instance.site)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.street = validated_data.get('street', instance.street)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.state = validated_data.get('state', instance.state)
    #     instance.lat = validated_data.get('lat', instance.lat)
    #     instance.lng = validated_data.get('lng', instance.lng)
    #     instance.save()
    #     return instance    
    
    
class GetRestaurantSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Restaurants
        fields = ('id', 'rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lng')

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

# class UpdateRestaurantSerializer(serializers.ModelSerializer):
    
#     class Meta: 
#         model = Restaurants
#         fields = ('id', 'rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lng')
#         extra_kwargs = {'id': {'required': False}}

#     def update(self, instance, validated_data):
#         instance.rating = validated_data.get('rating', instance.rating)
#         instance.name = validated_data.get('name', instance.name)
#         instance.site = validated_data.get('site', instance.site)
#         instance.email = validated_data.get('email', instance.email)
#         instance.phone = validated_data.get('phone', instance.phone)
#         instance.street = validated_data.get('street', instance.street)
#         instance.city = validated_data.get('city', instance.city)
#         instance.state = validated_data.get('state', instance.state)
#         instance.lat = validated_data.get('lat', instance.lat)
#         instance.lng = validated_data.get('lng', instance.lng)
#         instance.save()
#         return instance

class UpdateRestaurantSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Restaurants
        fields = ('id', 'rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lng')
        extra_kwargs = {'id': {'required': False}}   

class DeleteRestaurantSerializer(serializers.Serializer):
    id = serializers.CharField()

    
