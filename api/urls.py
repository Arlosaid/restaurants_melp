from django.urls import path

from api.views import get_restaurant, register_restaurant

urlpatterns = [
    path('register/', register_restaurant),
    path('get-restaurant/<int:id_restaurant>/', get_restaurant),
]