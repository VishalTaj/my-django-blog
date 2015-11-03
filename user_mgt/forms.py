from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
	username =forms.CharField(widget=forms.TextInput(attrs=
					{
					   'placeholder':'Enter username',
					}))
	password = forms.CharField(widget=forms.PasswordInput(attrs=
					{
					   'placeholder':'Enter Password',
					}))
	class Meta:
		model = User
		fields = ['username','password']
