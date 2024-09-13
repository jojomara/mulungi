# forms.py
from django import forms

class FlightBookingForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your full name'
    }))
    gender = forms.ChoiceField(choices=[('', '-- Select --'), ('M', 'Male'), ('F', 'Female')])
    dob = forms.DateField(widget=forms.TextInput(attrs={
        'placeholder': 'YYYY/MM/DD', 'type': 'date'
    }))
    nationality = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your nationality'
    }))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your phone number'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email address'
    }))
    passport_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your passport number'
    }))
    visa_document = forms.FileField()
    departure_city = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Enter departure city'
    }))
    destination_city = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Enter destination city'
    }))
