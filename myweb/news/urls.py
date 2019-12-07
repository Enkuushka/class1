from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('read/<int:news_id>/', views.read, name='read'),
    path('like/<int:news_id>/', views.like, name='like'),
]

