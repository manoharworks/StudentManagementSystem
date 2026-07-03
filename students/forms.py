from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        
        model = Student
        
        fields = [
            "name",
            "email",
            "phone",
            "date_of_birth",
            "gender",
            "address",
            "photo",
        ] 
        
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "date_of_birth": forms.DateInput(format="%Y-%M-%D", attrs={"class": "form-control", "type" : "date"}),
            "gender": forms.Select(attrs={"class": "form-select"}),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "photo": forms.ClearableFileInput(attrs={"class": "form-control"}),
            
        }