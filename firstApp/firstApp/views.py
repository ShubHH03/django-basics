from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, Django! You are in the home page.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, Django! You are in the about page.")

def contact(request):
    return HttpResponse("Hello, Django! You are in the contact page.")

