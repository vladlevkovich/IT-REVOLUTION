from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, Group, Permission
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
from ..core.models import RealEstate


class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = None
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    data_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'first_name']
    objects = CustomUserManager()

    groups = models.ManyToManyField(Group, blank=True, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_users')

    def __str__(self):
        return self.email

    def create_user(self):
        pass


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    real_estate = models.ForeignKey(RealEstate, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class DebitCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    number_card = models.CharField(max_length=16, blank=True, null=True)
    month_end = models.DateField()
    year_end = models.DateField()
    balance = models.PositiveIntegerField(default=25000)

    def __str__(self):
        return f'{self.user} - {self.number_card}'


