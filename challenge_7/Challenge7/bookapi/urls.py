from django.urls import path, include
from .views import bookviewsets, viewsets

urlpatterns = [
    path('', bookviewsets, name='index'),
    path('category/<str:category>/', viewsets, name='categories'),
]