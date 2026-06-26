from django.contrib import admin

from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        'client_name',
        'company',
        'rating',
        'is_active'
    )

    list_filter = (
        'rating',
        'is_active'
    )

    search_fields = (
        'client_name',
        'company'
    )
