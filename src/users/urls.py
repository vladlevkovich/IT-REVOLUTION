from django.urls import path
from .views import *


urlpatterns = [
    path('users/register/', CreateCustomUserView.as_view()),
    path('user-profile/', user_profile),
    path('update-user-profile/', user_update_profile)
]

