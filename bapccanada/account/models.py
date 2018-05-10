from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # email = models.EmailField(blank=False, unique=True)

    def __str__(self):
        return self.user.name
