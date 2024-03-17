from django import forms
from .models import BusinessAutomationInterne

class BusinessAutomationInterneForm(forms.ModelForm):
    class Meta:
        model = BusinessAutomationInterne
        
        # ordering Field name
        fields = ['first_name', 'last_name', 'dep', 'city', 'email']
        
        
        labels = {
            'dep': 'Department',
            'email': 'Email',
        }
        
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            'last_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            'dep': forms.TextInput(attrs={"class": "form-control", "placeholder": "Department"}),
            'city': forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}),
            'email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
        }
        
        
        error_messages = {
            'first_name': {'required': 'Enter your first name'},
            'last_name': {'required': 'Enter your last name'},
            'dep': {'required': 'Enter your Department'},
            'city': {'required': 'Enter your city'},
            'email': {'required': 'Enter your email'},
        }


