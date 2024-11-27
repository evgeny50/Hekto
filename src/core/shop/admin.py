from django.contrib import admin

from .models import Category, Product, Tag, PropertyKey, PropertyValue


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'slug')
    ordering = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'slug')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        return super().get_readonly_fields(request, obj)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description', 'category__name', 'tags__name')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description', 'price', 'sale_price', 'category', 'tags', 'available', 'stock')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),  # Makes this section collapsible
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # If the object already exists, make created_at and updated_at read-only
            return ['created_at', 'updated_at']
        return super().get_readonly_fields(request, obj)


@admin.register(PropertyKey)
class PropertyKeyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(PropertyValue)
class PropertyValueAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
    search_fields = ('key__name', 'value')
    list_filter = ('key',)


# @admin.register(ProductProperty)
# class ProductPropertyAdmin(admin.ModelAdmin):
#     list_display = ('product', 'get_property', 'get_value')
#     list_filter = ('property_value__key',)
#     search_fields = ('product__name', 'property_value__key__name', 'property_value__value')
#
#     def get_property(self, obj):
#         return obj.property_value.key.name
#     get_property.short_description = "Свойство"
#
#     def get_value(self, obj):
#         return obj.property_value.value
#     get_value.short_description = "Значение"
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        return super().get_readonly_fields(request, obj)