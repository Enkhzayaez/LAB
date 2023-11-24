from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from accountsApp.models import Account

class RegisterForm(ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
    }))
    repeat_password = forms.CharField(widget = forms.PasswordInput(attrs={
        'placeholder':'Repeat password',
    }))

    class Meta():
        model = User 
        fields = ('email', 'first_name', 'last_name', 'password', 'repeat_password')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = "Eter Email"
        self.fields['first_name'].widget.attrs['placeholder'] = "Eter FirstName"
        self.fields['last_name'].widget.attrs['placeholder'] = "Eter LastName"
        for fields in self.fields:
            self.fields[fields].widget.attrs['class'] = 'form-control'

class AccountsForm(ModelForm):
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder': 'Enter phone',
        'class': 'form-control',
    }))

    class Meta():
        model = Account
        fields = ('phone_number', 'profile_img')