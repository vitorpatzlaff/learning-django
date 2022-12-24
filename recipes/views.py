# Create your views here.

from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', status=200, context={
        'name': 'Vitor Hugo'
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', status=200, context={
        'name': 'Vitor Hugo'
    })
