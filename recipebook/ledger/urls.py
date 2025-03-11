from django.urls import path

from .views import recipe_list, recipe_detail, RecipeListView, RecipeDetailView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view, name='recipe-list'),
    path('recipe/1', RecipeDetailView.as_view, name='recipe-1')
]

app_name = 'ledger'