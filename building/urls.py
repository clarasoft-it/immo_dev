from django.urls import path
from . import views

urlpatterns = [
    path('buildings/', views.api_buildings, name='api_buildings'),
    path('buildings/<str:id>', views.api_GET_building, name='api_GET_building'),
]