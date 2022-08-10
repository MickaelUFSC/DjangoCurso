from django.http import HttpResponse


def home(request):
    return HttpResponse('HOME')


def contact(request):
    return HttpResponse('Contact')
