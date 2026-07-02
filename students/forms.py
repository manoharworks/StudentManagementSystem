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
        
           