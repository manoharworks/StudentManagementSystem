from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User 

class CustomUserCreationForm(UserCreationForm):
    
    first_name = forms.CharField(required = True, widget = forms.TextInput(attrs={"class" : "form-control"}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs= {"class": "form-control"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs= {"class": "form-control"}))  
    
    class Meta(UserCreationForm.Meta):
        model = User
        
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email') 
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        # Inject Bootstrap styling into the base username field dynamically
            if 'username' in self.fields:
                self.fields['username'].widget.attrs.update({'class': 'form-control'})
    