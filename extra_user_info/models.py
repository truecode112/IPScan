from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserExtraInfo(AbstractUser):
    signup_url = models.CharField(max_length=255, null=True, blank=True)