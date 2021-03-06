from django import forms
from django.contrib.auth.forms import UserCreationForm #username, password
from django.contrib.auth.models import User
from .models import RegisterUser

class RegistrationForm(UserCreationForm):
    #To add more imformation, simply define below and add it to fields
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class AdditionalForm(forms.ModelForm):
    class Meta:
        model = RegisterUser
        exclude = ('user', 'email_confirmed')

class LoginForm(forms.Form):
	username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class' : 'loginput'}),required=True)
	password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'loginput'}), required=True)
