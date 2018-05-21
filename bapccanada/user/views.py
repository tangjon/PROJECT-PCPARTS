from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView


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


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Profile'
        return context


class PreferencesView(TemplateView):
    template_name = 'preferences.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Preferences'
        return context


class CommentsView(TemplateView):
    template_name = 'comments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Comments'
        return context


class BuildsView(TemplateView):
    template_name = 'builds.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Builds'
        return context


class SecurityView(TemplateView):
    template_name = 'security.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Security'
        return context


class SavedView(TemplateView):
    template_name = 'saved.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Saved Parts'
        return context
