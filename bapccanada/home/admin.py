from django.contrib import admin
from products.models import GPU
from build.models import Build, Review

# Register your models here.
admin.site.register(GPU)
admin.site.register(Review)
admin.site.register(Build)

