from django.db import models
from django.template.defaultfilters import slugify

from polymorphic.models import PolymorphicModel


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

    def __str__(self):
        return "{} - {}".format(self.manufacturer, self.model_number)

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


class CPU(Component):
    cores = models.PositiveIntegerField(default=2)
    threads = models.PositiveIntegerField(default=4)
    series = models.CharField(max_length=100)
    socket = models.CharField(max_length=100)
    integrated_graphics = models.CharField(max_length=100, null=True)
    stock_freq = models.CharField(max_length=50)
    boost_freq = models.CharField(max_length=50)
    watts = models.CharField(max_length=50)
    l3_cache = models.CharField(max_length=20)

    def __str__(self):
        return "{} - {}".format(self.manufacturer, self.series)


class Monitor(Component):
    screen_size = models.PositiveIntegerField(default=10)
    resolution = models.CharField(max_length=100)
    aspect_ratio = models.CharField(max_length=100)
    response_time = models.CharField(max_length=100)
    refresh_rate = models.CharField(max_length=100)
    g_sync = models.CharField(max_length=100)
    dp_ports = models.IntegerField(default=0)
    hdmi_ports = models.IntegerField(default=0)
