from django.urls import re_path, path

from . import views

app_name = 'products'
urlpatterns = [
    path('gpu', views.gpu, name='gpu'),
]
