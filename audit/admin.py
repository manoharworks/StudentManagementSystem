from django.contrib import admin

from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):

    list_display = (
        "created_at",
        "user",
        "action",
        "content_type",
        "object_id",
        "object_repr",
    )

    list_filter = (
        "action",
        "content_type",
        "created_at",
    )

    search_fields = (
        "object_repr",
        "user__username",
    )

    readonly_fields = (
        "user",
        "action",
        "content_type",
        "object_id",
        "object_repr",
        "created_at",
    )
