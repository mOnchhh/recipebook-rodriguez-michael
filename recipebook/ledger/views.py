from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from .models import Ingredient, Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"


@login_required
class RecipeCreateView(CreateView):
    model = Recipe
    template_name = "recipe_form.html"
    fields = '__all__'

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = { "recipes": recipes }

    return render(request, 'recipe_list.html', ctx)

@login_required
def recipe_detail(request, pk):
    ctx = { "recipe": Recipe.objects.get(pk=pk) }
    return render(request, 'recipe_detail.html', ctx)

@login_required
def login_function(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            request,
            username = username,
            password = password
        )
        
        if user is not None:
            login(request, user)
            return redirect("recipe_list")
        else:
            login_error = "Invalid username or password"

def logout_function(request):
    logout(request)
    return redirect("recipe_list")
