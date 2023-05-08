from django.urls import path
from .views import *


urlpatterns = [
    path('home/', home),
    path('real-estate/<int:pk>/', detail),
    path('add-real-estate/', add_real_estate),
    path('real-estate-delete/<int:pk>/', delete_real_estate),
    path('real-estate-update/<int:pk>/', update_real_estates)
]
