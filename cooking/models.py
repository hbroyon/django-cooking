# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Ingredient(models.Model):
    """
    A model for the ingredients used for ours recipes.
    """
    name = models.CharField(max_length=512, verbose_name=_("Name"))
    price = models.PositiveIntegerField(verbose_name=_("Price"))


class RecipeDifficulty(models.Model):
    """
    A model to know the recipe difficulty.
    """
    difficulty = models.CharField(max_length=25, verbose_name=_("Difficulty"))


class RecipeType(models.Model):
    """
    A model to know the recipe type.
    """
    name = models.CharField(max_length=255, verbose_name=_("Name"))


class RecipePhoto(models.Model):
    """
    A model that contains the photo(s) of a recipe.
    """
    photo = models.ImageField(verbose_name=_("Photo"))


class Recipe(models.Model):
    """
    A model that describe a recipe.
    """
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    type = models.OneToOneField(RecipeType, verbose_name=_("Type"))
    difficulty = models.OneToOneField(RecipeDifficulty,
                                      verbose_name=_("Difficulty"))
    rating = models.PositiveIntegerField(verbose_name=_("Rating"))
    user = models.ForeignKey(User, verbose_name=_("User"))
    cost = models.PositiveIntegerField(verbose_name=_("Cost"))
    ingredients = models.ManyToManyField(Ingredient,
                                         verbose_name=_("Ingredients"))
    preparation_time = models.TimeField(verbose_name=_("Preparation Time"))
    cooking_time = models.TimeField(verbose_name=_("Cooking Time"))
    rest_time = models.TimeField(verbose_name=_("Rest Time"))
    photos = models.ManyToManyField(RecipePhoto, verbose_name=_("Photos"))


class RecipeComment(models.Model):
    """
    A model to comment the recipes.
    """
    title = models.CharField(max_length=75, verbose_name=_("Title"))
    comment = models.CharField(max_length=1200, verbose_name=_("Comment"))
    author = models.ForeignKey(User, verbose_name=_("Author"))
    recipe = models.ForeignKey(Recipe, verbose_name=_("Recipe"))
