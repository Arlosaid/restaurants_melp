from django.urls import path

from api.views import register_restaurant

urlpatterns = [
    path('register/', register_restaurant),
]