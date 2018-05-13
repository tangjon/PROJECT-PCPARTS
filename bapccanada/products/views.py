from django.shortcuts import render


def gpu(request):
    return render(request, 'gpu.html', {'title': 'Current Part List', 'slug': 'user'})
# Create your views here.
