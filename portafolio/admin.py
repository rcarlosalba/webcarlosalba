from django.contrib import admin
from .models import Projects, ProjectCategory
# Register your models here.


class ProjectCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'description', 'created', 'updated')
    search_fields = ('title', 'description', 'created', 'updated')
    date_hierarchy = 'created'
    list_filter = ('title', 'created', 'updated')

    def project_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])

    project_categories.short_description = 'Categorías'


admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Projects, ProjectAdmin)
