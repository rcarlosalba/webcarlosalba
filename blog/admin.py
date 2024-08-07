from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from .models import CategoryEntry, BlogEntry


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class BlogEntryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'content',
                     'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

    post_categories.short_description = "Categorías"


admin.site.register(CategoryEntry, CategoryAdmin)
admin.site.register(BlogEntry, BlogEntryAdmin)
