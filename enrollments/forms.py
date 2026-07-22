from django import forms
from .models import Enrollment


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment

        fields = [
            "student",
            "course",
            "academic_year",
            "semester",
            "status",
        ]

        widgets = {
            "student": forms.Select(attrs={"class": "forms-select"}),
            "course": forms.Select(attrs={"class": "forms-select"}),
            "academic_year": forms.TextInput(
                attrs={"class": "forms-control", "placeholder": "Academic Year"}
            ),
            "semester": forms.Select(
                attrs={
                    "class": "forms-select",
                }
            ),
            "status": forms.Select(
                attrs={"class": "forms-select", "placeholder": "Status"}
            ),
        }

    def clean(self):
        """
        Validate that the same student is not enrolled
        in the same course during the same academic year.
        """

        cleaned_data = super().clean()

        student = cleaned_data.get("student")
        course = cleaned_data.get("course")
        academic_year = cleaned_data.get("academic_year")

        # Only validate if all required fields are present
        if student and course and academic_year:
            queryset = Enrollment.objects.filter(
                student=student,
                course=course,
                academic_year=academic_year,
            )

            # Important: ignore the current object during update
            if self.instance.pk:
                queryset = queryset.exclude(pk=self.instance.pk)

            if queryset.exists():
                raise forms.ValidationError(
                    "This student is already enrolled in this course for the selected academic year."
                )

        return cleaned_data
