from django.contrib import admin

# Register your models here.
from account.models import UserProfile

admin.site.register(UserProfile)
