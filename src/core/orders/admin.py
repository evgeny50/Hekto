from django.contrib import admin

from core.shop.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('buyer__user__username', 'email', 'first_name', 'last_name')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('buyer', 'total_price', 'status', 'created_at')
        }),
        ('Contact Information', {
            'fields': ('first_name', 'last_name', 'email', 'address', 'postal_code', 'city')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # If the object already exists, make total_price and created_at read-only
            return ['created_at', 'total_price']
        return super().get_readonly_fields(request, obj)

