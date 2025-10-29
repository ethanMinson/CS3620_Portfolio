from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import BookData
from .serializer import BookSerializer
from rest_framework.pagination import LimitOffsetPagination
from django.core.paginator import Paginator

# Create your views here.

@api_view(['GET'])
def bookviewsets(request):
    books = BookData.objects.all()
    #serializer = BookSerializer(books, many=True)
    p = Paginator(books, 5)
    page = request.GET.get('page')
    books_page = p.get_page(page)

    pagination = LimitOffsetPagination()
    #return Response(serializer.data)
    return render(request, "books.html", {"books": books_page})

@api_view(['GET'])
def view_sets(request, category):
    books = BookData.objects.filter(category__iexact=category)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

class BookDataViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        book_specs = BookData.objects.all()
        return book_specs

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params)
        books= BookData.objects.filter(category__iexact=params['pk'])
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)