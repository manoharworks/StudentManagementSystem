from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course

        fields = [
            "code",
            "title",
            "credit_hours",
            "department",
            "semester",
            "description",
            "is_active",
        ]

        widgets = {
            "code": forms.TextInput(
                attrs={"class": "forms-control", "placeholder": "Course Code"}
            ),
            "title": forms.TextInput(
                attrs={"class": "forms-control", "placeholder": "Course Title"}
            ),
            "credit_hours": forms.TextInput(
                attrs={"class": "forms-control", "placeholder": "Course Credit_Hours"}
            ),
            "department": forms.Select(
                attrs={
                    "class": "forms-control",
                }
            ),
            "semester": forms.Select(
                attrs={"class": "forms-select", "placeholder": "Course Semester"}
            ),
            "description": forms.TextInput(
                attrs={"class": "forms-control", "placeholder": "Course Description"}
            ),
            "is_active": forms.TextInput(
                attrs={"class": "forms-control", "placeholder": "Course Is_Active"}
            ),
        }
