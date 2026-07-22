from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "title",
        "department",
        "semester",
        "credit_hours",
        "is_active",
    )

    list_filter = (
        "department",
        "semester",
        "is_active",
    )

    search_fields = (
        "code",
        "title",
    )

    ordering = (
        "semester",
        "code",
    )