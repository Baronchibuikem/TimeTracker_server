from django.contrib import admin
from accounts.models import CustomUser, Userprofile

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Userprofile)
