from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class soup_create(CreateView):
    model = Soup
    fields = '__all__'
    success_url = '/soups/{id}'

class soup_update(UpdateView):
    model = Soup
    fields = ['origin', 'temperature', 'broth']

class soup_delete(DeleteView):
    model = Soup
    success_url = '/soups'