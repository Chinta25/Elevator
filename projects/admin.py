from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'client',
        'location',
        'completion_date',
        'is_featured'
    )

    list_filter = (
        'location',
        'is_featured'
    )

    search_fields = (
        'title',
        'client',
        'location'
    )