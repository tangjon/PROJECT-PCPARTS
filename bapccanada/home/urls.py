from django.urls import re_path, path

from home.views import HomeView

from . import views

app_name = 'home'
urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home')
]
