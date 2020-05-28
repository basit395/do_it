from django.urls import path

from . import views

urlpatterns = [
    path('start/', views.start, name='start'),
    path('home/', views.start, name='start'),
    path('', views.index, name='index'),
]
