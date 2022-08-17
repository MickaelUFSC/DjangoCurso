
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', {
        'name': 'Mickael André'
    })


def category(request, id):
    return render(request, 'recipes/pages/category.html')