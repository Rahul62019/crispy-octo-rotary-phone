from django.shortcuts import render
from .models import Restaurant,Cuisine

# Create your views here.
def index(request):
    return render(request,"restaurants/index.html",{
        'restaurants': Restaurant.objects.all()
    })