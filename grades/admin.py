from django.contrib import admin

from .models import Grade


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):

    list_display = (
        "enrollment",
        "marks_obtained",
        "percentage",
        "letter_grade",
        "grade_point",
        "result",
    )

    list_filter = (
        "result",
        "letter_grade",
    )

    search_fields = (
        "enrollment__student__name",
        "enrollment__course__title",
    )

    autocomplete_fields = (
        "enrollment",
    )

    readonly_fields = (
        "percentage",
        "letter_grade",
        "grade_point",
        "result",
    )