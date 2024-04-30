from django.urls import path
from . import views

urlpatterns = [
    path('buildings/', views.api_buildings, name='api_buildings'),
    path('buildings/<str:id>', views.api_GET_building, name='api_GET_building'),
    path('buildings/<str:id>/units/', views.api_units, name='api_units'),
    path('buildings/<str:id>/units/<str:name>', views.api_GET_unit, name='api_GET_unit'),
    path('buildings/<str:id>/address', views.api_GET_buildingAddress, name='api_GET_buildingAddress'),
]