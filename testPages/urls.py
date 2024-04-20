from django.urls import path
from . import views

urlpatterns = [
    path('testPages/', views.immoTestPages, name='immoTestPages'),
    path('testPages/owner_create.html', views.createOwner, name='createOwner'),
    path('testPages/building_create.html', views.createBuilding, name='createBuilding'),
    path('testPages/index_Owners.html', views.indexOwners, name='indexOwners'),
    path('testPages/index_Buildings.html', views.indexBuildings, name='indexBuildings'),
]

