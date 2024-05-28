from django import forms 

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', widget=forms.TextInput())
    password = forms.CharField(label='User Password', widget=forms.PasswordInput())
    