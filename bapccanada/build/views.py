from django.shortcuts import render


def create(request):
    return render(request, 'create.html', {'title': 'Profile', 'slug': 'user'})
# Create your views here.
