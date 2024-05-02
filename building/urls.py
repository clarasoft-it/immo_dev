from django.urls import path
from . import views

urlpatterns = [
    path('buildings/', views.API_BuildingEnum, name='API_BuildingEnum'),
    path('buildings/<str:id>', views.API_BuildingInstance, name='API_Building'),
    path('buildings/owners', views.API_BuildingOwners, name='API_BuildingOwners'),
    path('buildings/<str:id>/address', views.API_BuildingAddress, name='API_BuildingAddress'),
    path('buildings/<str:id>/units/', views.API_UnitEnum, name='API_UnitEnum'),
    path('buildings/<str:id>/units/quoteShares', views.API_UnitQuoteShares, name='API_UnitQuoteShares'),
    path('buildings/<str:id>/units/<str:name>', views.API_UnitInstance, name='API_Unit'),
]