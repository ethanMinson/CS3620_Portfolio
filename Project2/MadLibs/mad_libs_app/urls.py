from django.urls import path, include

from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_protect

urlpatterns = [
    path('', views.index, name='index'),
    path('madlib/<slug:slug>/', views.madlib, name='madlib'),
]