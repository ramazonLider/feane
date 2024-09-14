from django.shortcuts import render
from .models import Category, Meal
# Create your views here.

def home(request):
    categories = Category.objects.all()
    meals = Meal.objects.all()

    data = {
    'categories': categories,
    'meals': meals,
    }
    return render(request, 'home.html', data)

def menu(request):
    categories = Category.objects.all()
    meals = Meal.objects.all()

    data = {
    'categories': categories,
    'meals': meals,
    }
    return render(request, 'menu.html', data)

def about(request):
    return render(request, 'about.html')
