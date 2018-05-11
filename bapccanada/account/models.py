from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class UserTest(User):
    age = models.IntegerField()
    birth_date = models.DateField()
