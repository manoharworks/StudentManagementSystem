from django.contrib import admin

from .models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "course",
        "academic_year",
        "semester",
        "status",
        "enrolled_at",
    )
    list_filter = (
        "status",
        "semester",
        "academic_year",
    )
    search_fields = (
        "student__name",
        "student__roll_number",
        "course__code",
        "course__title",
    )
    ordering = (
        "student__name",
        "course__code",
    )