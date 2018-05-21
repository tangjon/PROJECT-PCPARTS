from django.contrib import admin
from products.models import GPU, Review
from build.models import Build

# Register your models here.
admin.site.register(GPU)
admin.site.register(Review)
admin.site.register(Build)

