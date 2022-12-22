# Create your views here.

from django.http import HttpResponse


def home(request):
    return HttpResponse('HOME 2')


def contact(request):
    return HttpResponse('contato')


def about(request):
    return HttpResponse('sobre')
