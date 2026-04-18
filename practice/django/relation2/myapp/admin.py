from django.contrib import admin
from .models import Category, Product


# CATEGORY ADMIN
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


# PRODUCT ADMIN
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'qty', 'category', 'total']
    list_filter = ['category']
    search_fields = ['name']


# REGISTER MODELS
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)