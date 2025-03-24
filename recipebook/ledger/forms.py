from django import forms

from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'