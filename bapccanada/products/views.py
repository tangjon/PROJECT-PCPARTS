from django.shortcuts import render


def gpu(request):
    return render(request, 'gpuBrowse.html', {'title': 'Choose a Video Card', 'slug': 'user'})


def monitor(request):
    return render(request, 'monitor.html', {'title': 'Choose a Video Card', 'slug': 'user'})
# Create your views here.
