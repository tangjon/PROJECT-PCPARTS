from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView


class BaseProfileView(TemplateView):
    title_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title_name
        return context

    def dispatch(self, request, *args, **kwargs):
        # Todo WA: reverse by template name
        if request.path != reverse('user:' + self.template_name.split('.html')[0], kwargs={
            'username': request.user.username
        }):
            return redirect('home:home')
        return super(BaseProfileView, self).dispatch(request, *args, **kwargs)


class ProfileView(BaseProfileView):
    template_name = 'profile.html'
    title_name = 'Profile'


class PreferencesView(BaseProfileView):
    template_name = 'preferences.html'
    title_name = 'Preferences'


class CommentsView(BaseProfileView):
    template_name = 'comments.html'
    title_name = 'Comments'


class BuildsView(BaseProfileView):
    template_name = 'builds.html'
    title_name = 'Builds'


class SecurityView(BaseProfileView):
    template_name = 'security.html'
    title_name = 'Security'


class SavedView(BaseProfileView):
    template_name = 'saved.html'
    title_name = 'Saved Parts'
