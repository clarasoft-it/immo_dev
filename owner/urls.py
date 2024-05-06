from django.urls import path
from . import views

urlpatterns = [
    path('owners/', views.API_OwnerEnum, name='API_OwnerEnum'),
    path('owners/<str:id>', views.API_OwnerInstance, name='API_OwnerInstance'),

]