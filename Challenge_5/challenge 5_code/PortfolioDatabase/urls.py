from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("index", views.index, name="index"),
    path("", views.home, name="home"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("hobbies/", views.hobbies, name="hobbies"),
    path("contact/", views.contact, name="contact"),
    path("hobbies/detailed", views.hobbies_detailed, name="hobbies_detailed"),
    path("portfolio/detailed", views.portfolio_detailed, name="portfolio_detailed"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)