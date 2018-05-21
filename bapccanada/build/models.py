from django.db import models

from django.template.defaultfilters import slugify

from products.models import GPU, CPU, Monitor
from account.models import UserProfile


class Build(models.Model):
    gpu = models.ForeignKey(GPU, blank=True, on_delete=models.DO_NOTHING)
    cpu = models.ForeignKey(CPU, blank=True, on_delete=models.DO_NOTHING)
    monitor = models.ForeignKey(Monitor, blank=True, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, null=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Build, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.owner, self.name)





