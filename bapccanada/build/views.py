from django.shortcuts import render

from . import constants


def create(request):
    component_list = constants.get_components()

    return render(request, 'create.html', {'title': 'Current Part List',
                                           'component_list': component_list})
# Create your views here.
