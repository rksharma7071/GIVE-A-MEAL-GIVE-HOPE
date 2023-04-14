from django.db import models
from django.contrib.auth.models import User


class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default=True)
    description = models.TextField(default=True)
    website = models.URLField(default=True)
    address = models.CharField(max_length=200, default=True)
    phone_number = models.CharField(max_length=20, default=True)
    email_id = models.EmailField(max_length=30, default=True)

    def __str__(self):
        return self.user


class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default=True)
    description = models.TextField(default=True)
    website = models.URLField(default=True)
    address = models.CharField(max_length=200, default=True)
    phone_number = models.CharField(max_length=20, default=True)
    email_id = models.EmailField(max_length=30, default=True)