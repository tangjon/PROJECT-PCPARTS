from django.urls import re_path, path

from account.views import UserCreate, SignIn, Logout
from . import views

# lets follow reddit url format
# i.e /user/MrPotato
# .. /user/MrPotato/profile
# .. /user/MrPotato/preferences

app_name = 'account'
urlpatterns = [
    # path('user/', views.view_profile, name='profile'),
    # path('user/preferences/', views.view_preferences, name="preferences"),
    # path('user/comments/', views.view_comments, name="comments"),
    # path('user/builds/', views.view_builds, name="builds"),
    # path('user/notifications/', views.view_notifications, name="notifications"),
    # path('user/security/', views.view_security, name="security"),
    re_path(r'^signup/$', UserCreate.as_view(), name='sign_up'),
    re_path(r'^login/$', SignIn.as_view(), name="sign_in"),
    re_path(r'^logout/$', Logout.as_view(), name="logout"),

]
