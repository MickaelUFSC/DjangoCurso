from unicodedata import category

from django.urls import path

from recipes import views

urlpatterns = [

    path('', views.home),
    path('category/<slug:id>/', views.category),

]
