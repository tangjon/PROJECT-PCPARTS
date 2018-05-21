from django.urls import re_path, path

from account.views import UserCreate, SignIn, Logout
from . import views

# lets follow reddit url format
# i.e /user/MrPotato
# .. /user/MrPotato/profile
# .. /user/MrPotato/preferences

app_name = 'account'
urlpatterns = [
    re_path(r'^signup/$', UserCreate.as_view(), name='sign_up'),
    re_path(r'^login/$', SignIn.as_view(), name="sign_in"),
    re_path(r'^logout/$', Logout.as_view(), name="logout"),

]
