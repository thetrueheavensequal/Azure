from django import forms
from django.contrib.auth.models import User
from .models import Appointment, ContactMessage


class DateInput(forms.DateInput):
    input_type = 'date'


class AppmntForm(forms.ModelForm):
    class Meta:
        model = Appointment
        exclude = ['user', 'appmnt_on']
        widgets = {
            'appmnt_date': DateInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'c_name': 'Full Name',
            'c_phone': 'Phone Number',
            'c_email': 'Email Address',
            'e_name': 'Event Type',
            'appmnt_date': 'Preferred Date',
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 4}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
