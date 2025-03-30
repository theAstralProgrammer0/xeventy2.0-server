"""
This file registers the model with Django admin to let me easily add, modeify,
or delete articles without having to use a separate interface.
"""

from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

