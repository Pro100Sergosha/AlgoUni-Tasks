from django import forms 

class UserLoginForm(forms.Form):
    username = forms.CharField(label='User Name', widget=forms.TextInput({'class':'text-input'}))
    password = forms.CharField(label='User Password', widget= forms.PasswordInput({'class':'text-input'}))