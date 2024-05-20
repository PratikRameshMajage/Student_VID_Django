from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def student(request):
    return render(request, "student.html")

def card(request):
    return render(request, "card.html")

def contact(request):
    return render(request, "contact.html")

def signup(request):
    return render(request, "signup.html")

def signin(request):
    return render(request, "signin.html")