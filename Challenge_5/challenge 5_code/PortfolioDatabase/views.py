from django.http import HttpResponse
from django.shortcuts import render

from .models import Hobbies
from .models import Portfolio

def index(request):
    return HttpResponse("Hello, world. You're at the base index.")

def home(request):
    home_text = "Hello there. This is the home page of my Challenge 4 assignment.\nHi, my name is Ethan Minson. I am a Computer Science major at Weber State.\nI am in my senior year and set to graduate in the spring. I like playing board games and watching movies.\nI'm looking forward to learning a lot in this class."
    context = {"home_text": home_text}
    return render(request, "PortfolioDatabase/home.html", context)

def hobbies(request):
    hobbies_list = Hobbies.objects.all()
    context = {"hobbies_list": hobbies_list}
    return render(request, "PortfolioDatabase/hobbies.html", context)

def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    context = {"portfolio_list": portfolio_list}
    return render(request, "PortfolioDatabase/portfolio.html", context)

def contact(request):
    contact_text = "email: ethanminson@mail.weber.edu"
    context = {"contact_text": contact_text}
    return render(request, "PortfolioDatabase/contact.html", context)

def hobbies_detailed(request):
    hobbies_list = Hobbies.objects.all()
    context = {"hobbies_list": hobbies_list}
    return render(request, "PortfolioDatabase/hobbies_detailed.html", context)

def portfolio_detailed(request):
    portfolio_list = Portfolio.objects.all()
    context = {"portfolio_list": portfolio_list}
    return render(request, "PortfolioDatabase/portfolio_detailed.html", context)
