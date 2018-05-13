from django.db import models
from django.template.defaultfilters import slugify

from polymorphic.models import PolymorphicModel

from account.models import UserProfile


class Component(PolymorphicModel):
    manufacturer = models.CharField(max_length=30)
    model_number = models.CharField(max_length=30, unique=True)
    serial_number = models.CharField(max_length=30, blank=True)
    cheapest_store = models.CharField(max_length=30, blank=True)
    store_link = models.URLField(max_length=300, blank=True)

    price = models.IntegerField(default=0)
    release_year = models.PositiveIntegerField(default=2000)
    shipping_cost = models.PositiveIntegerField(default=0)

    last_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.model_number)
        super(Component, self).save(*args, **kwargs)


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


class Build(models.Model):
    gpu = models.ManyToManyField(GPU)
    name = models.CharField(max_length=100, null=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Build, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.owner, self.name)


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
