from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.App, name='app'),
    path('app/owner_index', views.AppOwnerIndex, name='AppOwnerIndex'),
    path('app/owner_info/<str:id>', views.AppOwnerInfo, name='AppOwnerInfo'),
    path('app/owner_create.html', views.AppOwnerCreate, name='AppOwnerCreate'),
    path('app/building_index', views.AppBuildingIndex, name='AppBuildingIndex'),
    path('app/building_info/<str:id>', views.AppBuildingInfo, name='AppBuildingInfo'),
    path('app/building_create.html', views.AppBuildingCreate, name='AppBuildingCreate'),

]
