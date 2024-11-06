from django import forms
from django.contrib.auth.forms import UserCreationForm
from Userauths.models import User

class RegisterForm(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
  email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
  phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

  class Meta:
    model = User
    fields = ['username', 'email', 'phone_number']