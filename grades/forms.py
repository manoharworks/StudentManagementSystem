from django import forms

from .models import Grade


class GradeForm(forms.ModelForm):

    class Meta:

        model = Grade

        fields = [
            "enrollment",
            "marks_obtained",
            "maximum_marks",
            "remarks",
        ]

        widgets = {

            "enrollment": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "marks_obtained": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "maximum_marks": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),
            
        }    