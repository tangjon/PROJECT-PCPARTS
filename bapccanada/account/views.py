from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView

from account.forms import SignUpForm
from account.models import UserProfile
from django.contrib.auth import login as auth_login
title = 'User Page'


def view_profile(request):
    return render(request, 'profile.html', {'title': 'Profile', 'slug': 'user'})


def view_preferences(request):
    return render(request, 'preferences.html', {'title': 'Preferences', 'slug': 'preferences'})


def view_comments(request):
    return render(request, 'comments.html', {'title': 'Preferences', 'slug': 'comments'})


def view_builds(request):
    return render(request, 'builds.html', {'title': 'Preferences', 'slug': 'builds'})


def view_notifications(request):
    return render(request, 'notifications.html', {'title': 'Preferences', 'slug': 'notifications'})


def view_security(request):
    return render(request, 'security.html', {'title': 'Preferences', 'slug': 'security'})


class UserCreate(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auth_login(request, user)
            return redirect('home:home')
        return redirect('account:sign_up')
