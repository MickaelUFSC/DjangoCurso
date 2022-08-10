from django.urls import path

from recipes.views import contact, home

urlpatterns = [

    path('', home),
    path('contact/', contact)
]
