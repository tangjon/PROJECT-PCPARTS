from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView


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
