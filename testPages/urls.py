from django.urls import path
from . import views

urlpatterns = [
    path('testPages/', views.immoTestPages, name='immoTestPages'),
    path('testPages/owner_create.html', views.createOwner, name='createOwner'),
    path('testPages/building_create.html', views.createBuilding, name='createBuilding'),
]

