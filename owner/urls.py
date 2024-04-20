from django.urls import path
from . import views

urlpatterns = [
    path('owners/', views.owners, name='owners'),
    path('owners/<str:id>', views.owner_info, name='owner_info'),
]