from django.contrib import admin

from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    list_display = (
        "enrollment",
        "date",
        "status",
    )

    list_filter = (
        "status",
        "date",
    )

    search_fields = (
        "enrollment__student__name",
        "enrollment__course__title",
    )

    autocomplete_fields = (
        "enrollment",
    )

    ordering = (
        "-date",
    )