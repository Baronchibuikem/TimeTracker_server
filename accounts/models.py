from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(null=True, blank=True, max_length=50)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Userprofile(models.Model):
    user = models.ForeignKey(
        CustomUser, related_name="userprofile", on_delete=models.CASCADE)
    active_team_id = models.IntegerField(null=True, blank=True)
