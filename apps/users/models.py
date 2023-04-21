from django.db import models
from django.contrib.auth.models import AbstractUser


class StoreUser(AbstractUser):
    CHOICES_WHO = [
        ('ПРОДАВЕЦ', 'ПРОДАВЕЦ'),
        ('ПОКУПАТЕЛЬ', 'ПОКУПАТЕЛЬ'),
    ]
    phone_number = models.CharField(max_length=20)

    user_who = models.CharField(max_length=10, choices=CHOICES_WHO)

    REQUIRED_FIELDS = ['user_who']

