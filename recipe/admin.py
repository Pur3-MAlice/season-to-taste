from django.contrib import admin
from .models import Recipe, Season, Diet
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Diet)

admin.site.register(Season)


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', 'ingredients')
