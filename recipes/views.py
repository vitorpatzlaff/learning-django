# Create your views here.

from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', status=200, context={
        'name': 'Vitor Hugo'
    })
