from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    subscription = models.CharField(max_length=50, default=' ', null=True, blank=True)
    user_cell_phone = models.CharField(max_length=50, default=' ', null=True, blank=True)
