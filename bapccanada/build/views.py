from django.shortcuts import render


def create(request):
    return render(request, 'create.html', {'title': 'Current Part List', 'slug': 'user'})
# Create your views here.
