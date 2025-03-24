from django.contrib import admin

from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ("name",)
    image = RecipeImage
    inlines = [RecipeIngredientInline]

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name',)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)