from django.shortcuts import render

# Create your views here.
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


def view_saved(request):
    return render(request, 'saved.html', {'title': 'Preferences', 'slug': 'saved'})