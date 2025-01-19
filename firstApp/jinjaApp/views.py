from django.shortcuts import render
from .models import Cars

# Create your views here.
def jinja(request):
    cars = Cars.objects.all()
    return render(request, 'jinjaApp/jinja.html',{'cars':cars})
