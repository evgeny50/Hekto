from django.contrib import admin

from .models import Category, Product, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'image', 'price', 'available')
    list_editable = ('price', 'available')
    list_display_links = ('pk', 'name',)
    list_filter = ('name', 'price', 'available', 'updated')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)