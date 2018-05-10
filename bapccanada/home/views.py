from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

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
