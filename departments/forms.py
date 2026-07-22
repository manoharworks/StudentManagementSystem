from django import forms 
from .models import Department

class DepartmentForm(forms.ModelForm):
    
    class Meta:
        
        model = Department
        
        fields = [
            "name",
            "code",
            "description", 
        ]
        
        widgets = {
            "name": forms.TextInput(attrs={"class" :  "form-control", "placeholder" : "Department Name"}),
            "code": forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Department Code"}),
            "description": forms.Textarea(attrs={"class" : "form-control", "placeholder" : "Department Description "}),    
        }