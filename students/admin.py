from django.contrib import admin
from .models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "roll_number",
        "name",
        "department",
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
        "roll_number", "name"
    )