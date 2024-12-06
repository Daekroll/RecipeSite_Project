from django.contrib import admin

from .models import Recipe, Category


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description_short", "steps_short", "time", "author", "ingredients_short", "category", "date_create"
    list_display_links = "pk", "name"
    ordering = "pk", "-name"
    search_fields = "name", "description", "category",

    @classmethod
    def description_short(cls, obj: Recipe) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."

    def steps_short(cls, obj: Recipe) -> str:
        if len(obj.steps) < 48:
            return obj.steps
        return obj.steps[:48] + "..."

    def ingredients_short(cls, obj: Recipe) -> str:
        if len(obj.ingredients) < 48:
            return obj.ingredients
        return obj.ingredients[:48] + "..."

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description"
    list_display_links = "pk", "name"
    ordering = "pk", "-name"
