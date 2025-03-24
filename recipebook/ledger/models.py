from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    update_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("recipe_detail", args=[str(self.pk)])

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        null=True,
        related_name="ingredients"
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        null=True,
        related_name="recipe"
    )
        
    def __str__(self):
        return f"{self.quantity} {self.ingredient.name} for {self.recipe.name}"

class RecipeImage(models.Model):
    image = models.ImageField(upload_to="images/")
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        null=True,
        related_name="images"
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
