from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Soup, Ingredients
from .forms import MealForm

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
    soup_ings = soup.ingredients.all().values_list('id')
    excluded_ings = Ingredients.objects.exclude(id__in=soup_ings)
    meal_form = MealForm()
    return render(request, 'soups/detail.html', {
        'soup': soup,
        'meal_form': meal_form,
        'ingredients': excluded_ings
    })

class soup_create(CreateView):
    model = Soup
    fields = ['name', 'origin', 'temperature', 'broth']
    success_url = '/soups/{id}'

class soup_update(UpdateView):
    model = Soup
    fields = ['origin', 'temperature', 'broth']

class soup_delete(DeleteView):
    model = Soup
    success_url = '/soups'

def add_meal(request, soup_id):
    meal_form = MealForm(request.POST)

    if meal_form.is_valid():
        new_meal = meal_form.save(commit=False)
        new_meal.soup_id = soup_id
        new_meal.save()
    
    return redirect('detail', soup_id=soup_id)

def ing_index(request):
    ingredients = Ingredients.objects.all()
    return render(request, 'main_app/ing_list.html', { 'ingredients': ingredients })

def ing_detail(request, ing_id):
    ingredient = Ingredients.objects.get(id=ing_id)
    return render(request, 'main_app/ing_detail.html', { 'ingredient': ingredient })

class ing_create(CreateView):
    model = Ingredients
    fields = '__all__'
    success_url = '/ingredients/{id}'

class ing_edit(UpdateView):
    model = Ingredients
    fields = ['name', 'food_group']

class ing_delete(DeleteView):
    model = Ingredients
    success_url = '/ingredients'

def assoc_ing(request, soup_id, ing_id):
    Soup.objects.get(id=soup_id).ingredients.add(ing_id)
    return redirect('detail', soup_id=soup_id)

def unassoc_ing(request, soup_id, ing_id):
    Soup.objects.get(id=soup_id).ingredients.remove(ing_id)
    return redirect('detail', soup_id=soup_id)