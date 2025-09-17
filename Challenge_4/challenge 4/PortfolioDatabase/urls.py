from django.urls import path

from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("", views.home, name="home"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("hobbies/", views.hobbies, name="hobbies"),
    path("contact/", views.contact, name="contact"),
]