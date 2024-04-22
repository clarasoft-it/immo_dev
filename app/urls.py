from django.urls import path
from . import views

urlpatterns = [
    path('app/<str:langid>', views.App, name='app'),
    path('app/<str:langid>/owner_index', views.AppOwnerIndex, name='AppOwnerIndex'),
    path('app/<str:langid>/owner_info/<str:id>', views.AppOwnerInfo, name='AppOwnerInfo'),
    path('app/<str:langid>/owner_create.html', views.AppOwnerCreate, name='AppOwnerCreate'),
    path('app/<str:langid>/building_index', views.AppBuildingIndex, name='AppBuildingIndex'),
    path('app/<str:langid>/building_info/<str:id>', views.AppBuildingInfo, name='AppBuildingInfo'),
    path('app/<str:langid>/building_create.html', views.AppBuildingCreate, name='AppBuildingCreate'),

]
