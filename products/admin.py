from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'capacity',
        'is_featured',
        'created_at'
    )

    list_filter = (
        'category',
        'is_featured'
    )

    search_fields = (
        'title',
        'category'
    )

    prepopulated_fields = {
        'slug': ('title',)
    }
