from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .models import Recipe


class RecipeView(ListView):
    queryset = Recipe.objects.order_by('?').select_related('category')[:5]
    template_name = 'recipe/index.html'


class CreateRecipeView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipe/create_recipe.html'
    fields = 'name', 'description', 'time', 'steps', 'image', 'ingredients', 'category'
    success_url = reverse_lazy('recipe:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateRecipeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    template_name = 'recipe/update_recipe.html'
    fields = 'name', 'description', 'time', 'steps', 'image', 'ingredients', 'category'
    success_url = reverse_lazy('recipe:index')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author or self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('recipe:index')

class DetailRecipeView(DetailView):
    queryset = Recipe.objects.select_related('category')
    template_name = 'recipe/detail_recipe.html'

