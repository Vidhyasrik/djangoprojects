from django.db import models
from django.utils import timezone
from django.db.models import CharField, DateTimeField, TextField
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    # Custom fields
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=255, unique=True)
    last_login = DateTimeField(default=timezone.now)


