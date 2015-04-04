# -*- coding: utf-8 -*-
from django.contrib import admin

from cooking.models import Ingredient, RecipeDifficulty, RecipeType, \
    RecipePhoto, Recipe, RecipeComment


# Register your models here.
admin.site.register(Ingredient)
admin.site.register(RecipeDifficulty)
admin.site.register(RecipeType)
admin.site.register(RecipePhoto)
admin.site.register(Recipe)
admin.site.register(RecipeComment)
