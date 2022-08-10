from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', {
        'name': 'Mickael André'
    })


def contact(request):
    return HttpResponse('Contact')
