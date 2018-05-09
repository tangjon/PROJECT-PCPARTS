from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import SignUpForm


class HomeView(TemplateView):
    template_name = 'home.html'


def home_view(request):
    return render(request, 'home.html', {'title': 'Home'})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('home:home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'title': 'Login', 'form': form})


def signup_view(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save();
            return redirect('home:signup')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
