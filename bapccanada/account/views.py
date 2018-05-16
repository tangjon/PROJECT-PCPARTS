from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView

from account.forms import SignUpForm
from account.models import UserProfile
from django.contrib.auth import login as auth_login

title = 'User Page'


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('home:home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'title': 'Login', 'form': form})


class UserCreate(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home:home')
        return redirect('account:sign_up')


class SignIn(LoginView):
    template_name = 'signin.html'
    redirect_authenticated_user = True

class Logout(LogoutView):
    template_name = 'logout.html'
    next_page = 'home:home'
