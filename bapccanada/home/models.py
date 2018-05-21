from django.db import models


class Price(models.Model):
    price = models.IntegerField(default=0)
    store = models.CharField(max_length=100)
    store_link = models.URLField()


class Image(models.Model):
    image_link = models.URLField()

