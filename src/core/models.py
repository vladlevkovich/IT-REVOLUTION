from django.conf import settings
from django.db import models


class RealEstate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    number_rooms = models.IntegerField(default=1)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_sold = models.BooleanField(default=False)    # продана нерухомість чи ні
    is_active_in_lease = models.BooleanField(default=True)  # чи активна нерухомість
    in_rent = models.BooleanField(default=False)    # чи в оренді нерухомість
    prepared_for_rent = models.BooleanField(default=True)   # підготовлено до здачі в оренду
    is_archived = models.BooleanField(default=False)    # власник не бажає розміщувати даний об'єкт

    def __str__(self):
        return self.title


