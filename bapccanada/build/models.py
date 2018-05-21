from django.db import models

from django.template.defaultfilters import slugify

from products.models import Component, GPU, CPU
from account.models import UserProfile
from . import constants


class Build(models.Model):
    gpu = models.ManyToManyField(GPU)
    cpu = models.ManyToManyField(CPU)
    name = models.CharField(max_length=100, null=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Build, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.owner, self.name)

    def generate_component_table(self):
        allowed_parts = constants.get_components()


class Review(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    build = models.ForeignKey(Build, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=1000)
    stars = models.PositiveIntegerField(default=0)
    time_added = models.DateTimeField(auto_now=True)
    time_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.user, self.id)


