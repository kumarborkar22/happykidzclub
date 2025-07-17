from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['guardian_name', 'guardian_email', 'child_name', 'child_age', 'message']
        widgets = {
            'guardian_name': forms.TextInput(attrs={'class': 'form-control border-0', 'placeholder': 'Guardian Name'}),
            'guardian_email': forms.EmailInput(attrs={'class': 'form-control border-0', 'placeholder': 'Guardian Email'}),
            'child_name': forms.TextInput(attrs={'class': 'form-control border-0', 'placeholder': 'Child Name'}),
            'child_age': forms.TextInput(attrs={'class': 'form-control border-0', 'placeholder': 'Child Age'}),
            'message': forms.Textarea(attrs={'class': 'form-control border-0', 'placeholder': 'Leave a message here', 'style': 'height: 100px'}),
        }