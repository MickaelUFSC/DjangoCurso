from django.urls import path

from recipes import views

urlpatterns = [

    path('', views.home),
    path('informations/<slug:id>/', views.informations),

]
