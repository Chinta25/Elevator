from django.contrib import admin
from .models import Quotation


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'phone',
        'lift_type',
        'city',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
        'lift_type',
        'city'
    )

    search_fields = (
        'name',
        'phone',
        'email'
    )