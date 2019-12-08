from django.urls import path, include

from . import views

urlpatterns = [
    path('index', views.index, name='hereglegch.index'),
    path('burtgel', views.burtgel, name='burtgel'),
]

