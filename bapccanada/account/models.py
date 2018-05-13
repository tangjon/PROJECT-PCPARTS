from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     birth_date = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return self.user.username


#
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:m
#         UserProfile.objects.create(user=instance)
#     instance.profile.save()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#     instance.userprofile.save()
