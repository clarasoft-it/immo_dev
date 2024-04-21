from django.urls import path
from . import views

urlpatterns = [
    path('owners/', views.api_owners, name='api_owners'),
    path('owners/<str:id>', views.api_GET_owner, name='api_GET_owner'),

]