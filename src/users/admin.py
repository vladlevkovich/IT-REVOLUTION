from django.contrib import admin
from .models import CustomUser, UserProfile, DebitCart

admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(DebitCart)
