from django.urls import re_path, path

from . import views

app_name = 'products'
urlpatterns = [
    path('gpu/', views.gpu, name='gpu'),
    path('cpu/', views.cpu, name='cpu'),
    path('monitor/', views.monitor, name='monitors'),
    path('gpu/monitor', views.monitor, name='monitor')
]
