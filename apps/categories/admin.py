from django.contrib import admin

from apps.categories.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Category, CategoryAdmin)