from django.shortcuts import render
from .models import Soup

# soups = [
#     {'name': 'Clam Chowder', 'origin': 'Boudin SF', 'ingredients': ['Clams', 'Potatoes', 'Sourdough']},
#     {'name': 'Pho', 'origin': 'Homemade', 'ingredients': ['Flank Steak', 'Rice Noodles', 'Bean Sprouts']},
# ]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def soup_index(request):
    soups = Soup.objects.all()
    return render(request, 'soups/index.html', {
        'soups': soups,
    })

def soup_detail(request, soup_id):
    soup = Soup.objects.get(id = soup_id)
    return render(request, 'soups/detail.html', {
        'soup': soup,
    })