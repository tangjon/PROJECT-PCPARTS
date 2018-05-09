from django.shortcuts import render


def create(request):
    return render(request, 'create.html', {'title': 'Start a build', 'slug': 'user'})
# Create your views here.
