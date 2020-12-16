from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Userprofile(models.Model):
    user = models.ForeignKey(
        CustomUser, related_name="userprofile", on_delete=models.CASCADE)
    active_team_id = models.IntegerField()
