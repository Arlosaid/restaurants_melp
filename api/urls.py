from django.urls import path

from api.views import  delete_restaurant, get_restaurant, register_restaurant, update_restaurant

urlpatterns = [
    path('register/', register_restaurant),
    path('get-restaurant/<str:id_restaurant>/', get_restaurant),
    path('update-restaurant/<str:id>/', update_restaurant),
    path('delete-restaurant/<str:id>/', delete_restaurant),
]