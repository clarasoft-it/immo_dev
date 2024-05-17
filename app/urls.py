from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppIndex, name='AppIndex'),
    path('app/<str:langid>/login', views.AppLogin, name='AppLogin'),
    path('app/<str:langid>', views.App, name='App'),
    path('app/<str:langid>/owner_index', views.AppOwnerIndex, name='AppOwnerIndex'),
    path('app/<str:langid>/owner_create.html', views.AppOwnerCreate, name='AppOwnerCreate'),
    path('app/<str:langid>/building_index', views.HTML_PAGE_AppBuildingIndex, name='HTML_PAGE_AppBuildingIndex'),
    path('app/<str:langid>/building_info/<str:id>', views.HTML_PAGE_AppBuildingInfo, name='HTML_PAGE_AppBuildingInfo'),
    path('app/<str:langid>/building_create.html', views.HTML_PAGE_AppBuildingCreate, name='HTML_PAGE_AppBuildingCreate'),
    path('app/<str:langid>/<str:building_id>/unit_create.html', views.AppUnitCreate, name='AppUnitCreate'),
    path('app/<str:langid>/buildings/buildingInfoTable', views.HTML_SECTION_AppBuildingIndexTable, name='HTML_SECTION_AppBuildingIndexTable'),
    path('app/<str:langid>/owners/ownerInfoTable', views.HTML_SECTION_AppOwnerIndexTable, name='HTML_SECTION_AppOwnerIndexTable'),
    path('app/<str:langid>/ownerList', views.HTML_SECTION_OwnerList, name='HTML_SECTION_OwnerList'),
    path('app/<str:langid>/buildings/<str:building_id>/unitTable', views.HTML_SECTION_UnitTable, name='HTML_SECTION_UnitTable'),

    path('app/<str:langid>/building_wizard', views.HTML_PAGE_AppBuildingWizard, name='HTML_PAGE_AppBuildingWizard'),

]



