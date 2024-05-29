from django.shortcuts import render

soups = [
    {'name': 'Clam Chowder', 'origin': 'Boudin SF', 'ingredients': ['Clams', 'Potatoes', 'Sourdough']},
    {'name': 'Pho', 'origin': 'Homemade', 'ingredients': ['Flank Steak', 'Rice Noodles', 'Bean Sprouts']},
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def soup_index(request):
    return render(request, 'soups/index.html', {
        'soups': soups,
    })