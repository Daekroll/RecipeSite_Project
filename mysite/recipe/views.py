from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .models import Recipe, Category


class RecipeView(ListView):
    queryset = Recipe.objects.order_by('?').select_related('category')[:5]
    template_name = 'recipe/index.html'


class CreateRecipeView(CreateView):
    model = Recipe
    template_name = 'recipe/create_recipe.html'
    fields = '__all__'
    success_url = reverse_lazy('recipe:index')


class UpdateRecipeView(UpdateView):
    model = Recipe
    template_name = 'recipe/update_recipe.html'
    fields = 'name', 'description', 'time', 'steps', 'image', 'ingredients', 'category'
    success_url = reverse_lazy('recipe:index')


class DetailRecipeView(DetailView):
    queryset = Recipe.objects.select_related('category')
    template_name = 'recipe/detail_recipe.html'


class CreateCategoryView(CreateView):
    model = Category
    template_name = 'recipe/create_category.html'
    fields = '__all__'
    success_url = reverse_lazy('recipe:index')
