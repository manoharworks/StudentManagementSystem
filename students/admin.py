from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "gender",
    )
    
    search_fields = (
        "name",
        "email",
        "phone",
    )
    
    list_filter = (
        "gender",
    )
    
    ordering = (
        "name",
    )