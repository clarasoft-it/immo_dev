from django.urls import path
from . import views

urlpatterns = [
    path('buildings/', views.buildings, name='buildings'),
    path('buildings/<str:id>', views.building_info, name='building_info'),
]