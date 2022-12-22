# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'global/home.html')


def contact(request):
    return HttpResponse('contato')


def about(request):
    return HttpResponse('sobre')
