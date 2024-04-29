from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppIndex, name='AppIndex'),
    path('app/<str:langid>/login', views.AppLogin, name='AppLogin'),
    path('app/<str:langid>', views.App, name='App'),
    path('app/<str:langid>/owner_index', views.AppOwnerIndex, name='AppOwnerIndex'),
    path('app/<str:langid>/owner_info/<str:id>', views.AppOwnerInfo, name='AppOwnerInfo'),
    path('app/<str:langid>/owner_create.html', views.AppOwnerCreate, name='AppOwnerCreate'),
    path('app/<str:langid>/building_index', views.AppBuildingIndex, name='AppBuildingIndex'),
    path('app/<str:langid>/building_info/<str:id>', views.AppBuildingInfo, name='AppBuildingInfo'),
    path('app/<str:langid>/building_create.html', views.AppBuildingCreate, name='AppBuildingCreate'),
    path('app/<str:langid>/<str:building_id>/unit_create.html', views.AppUnitCreate, name='AppUnitCreate'),

]
