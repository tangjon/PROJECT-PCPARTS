from django.contrib.auth.decorators import login_required
from django.urls import re_path, path

from account.views import UserCreate, SignIn, Logout
from user.views import ProfileView, PreferencesView, BuildsView, CommentsView, SecurityView, SavedView
from . import views

# lets follow reddit url format
# i.e /user/MrPotato
# .. /user/MrPotato/profile
# .. /user/MrPotato/preferences
app_name = 'user'
urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('preferences/', PreferencesView.as_view(), name="preferences"),
    path('comments/', CommentsView.as_view(), name="comments"),
    path('builds/', BuildsView.as_view(), name="builds"),
    path('security/', SecurityView.as_view(), name="security"),
    path('saved/', SavedView.as_view(), name="saved")
]
