from django import forms
from .models import Attendance


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance

        fields = [
            "enrollment",
            "date",
            "status",
            "remarks"
        ]

        widgets = {
            "enrollment": forms.Select(attrs={"class": "form-select"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "remarks": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Optional Remarks"}),
        }

    def clean(self):
        cleaned_data= super().clean()
        
        enrollment = cleaned_data.get("enrollment")
        date = cleaned_data.get("date")
        
        if enrollment and date:
            queryset = Attendance.objects.filter(
                enrollment=enrollment,
                date=date,
            )
        
            if self.instance.pk:
                queryset = queryset.exclude(pk=self.instance.pk)

            if queryset.exists():
                self.add_error(
                    "date", 
                    "An attendance record already exists for this student on this specific date."
                )

        return cleaned_data
