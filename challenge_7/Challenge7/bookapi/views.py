from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BookData
from .serializer import BookSerializer

# Create your views here.

@api_view(['GET'])
def bookviewsets(request):
    books = BookData.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewsets(request, category):
    books = BookData.objects.filter(category__iexact=category)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)