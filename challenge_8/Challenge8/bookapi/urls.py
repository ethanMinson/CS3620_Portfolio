from django.urls import path, include
from .views import bookviewsets, view_sets, BookDataViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', BookDataViewSet, basename='books')

urlpatterns = [
    #path('', bookviewsets, name='index'),
    path('category/<str:category>/', view_sets, name='categories'),
    path('',include(router.urls)),
    #path('books/', BookDataViewSet.as_view({'get':'list'}), name='search'),
]