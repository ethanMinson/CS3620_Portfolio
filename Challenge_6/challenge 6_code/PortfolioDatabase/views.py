from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django import forms

from .contactForm import ContactForm, ContactModelForm,PortfolioAdd,PortfolioEdit
from .models import Hobbies
from .models import Portfolio
from .models import Contact

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
def portfolio_view(request, slug):
    project = Portfolio.objects.get(slug=slug)
    return render(request, "PortfolioDatabase/portfolio_detailed.html", {"project": project})
#make needed changes to the below views
@login_required(login_url="/login")
def portfolio_edit(request, slug):
    instance = Portfolio.objects.get(slug=slug)
    if request.method == "POST":
        form = PortfolioEdit(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("portfolio")
    else:
        form = PortfolioEdit(instance=instance)
    return render(request, "PortfolioDatabase/portfolio_edit.html", {"form": form})
@login_required(login_url="/login")
def portfolio_delete(request, slug):
    project = Portfolio.objects.get(slug=slug)

    if request.method == "POST":
        project.delete()
        if "next" in request.POST:
            return redirect(request.POST.get("next"))
        else:
            return redirect("/portfolio")
    return render(request, "PortfolioDatabase/portfolio_delete.html", {"project": project})

class AddPortfolio(FormView):
    template_name = "PortfolioDatabase/portfolio_add.html"
    form_class = PortfolioAdd
    success_url = "/portfolio"

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class ContactFormView(FormView):
    template_name = "PortfolioDatabase/contact_create.html"
    form_class = ContactModelForm
    success_url = "/contact"

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class ContactListView(ListView):
    model = Contact
    context_object_name = "contact_list"

    def render_to_response(self, context, **response_kwargs):
        contacts = ''
        for cntct in context["contact_list"]:
            contacts += f'<li>{cntct.name}---{cntct.email}</li>'
        return HttpResponse(f'<html><ul>{contacts}</ul></html>')

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "PortfolioDatabase/login.html", {"form":form})
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    return render(request, "PortfolioDatabase/logout.html")
def create_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("/")
    else:
        form = UserCreationForm()
    return render (request, "PortfolioDatabase/create-account.html", {"form": form})
