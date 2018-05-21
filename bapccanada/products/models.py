from django.db import models
from django.template.defaultfilters import slugify

from account.models import UserProfile
from build.models import Component
from build.models import Build


class GPU(Component):
    clock_rate = models.PositiveIntegerField(default=1000)
    clock_rate_oc = models.PositiveIntegerField(default=0)
    cuda_cores = models.PositiveIntegerField(default=2)
    hdmi_ports = models.PositiveIntegerField(default=0)
    vga_ports = models.PositiveIntegerField(default=0)
    dp_ports = models.PositiveIntegerField(default=0)

    overclocked = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.manufacturer, self.model_number)


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
