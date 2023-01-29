from django.urls import path

from api.views import DeleteRestaurantView, get_restaurant, register_restaurant, UpdateRestaurantView

urlpatterns = [
    path('register/', register_restaurant),
    path('get-restaurant/<str:id_restaurant>/', get_restaurant),
    path('update-restaurant/<str:id>/', UpdateRestaurantView.as_view()),
    path('delete-restaurant/<str:id>/', DeleteRestaurantView.as_view()),
]