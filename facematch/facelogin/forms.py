from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
	email=forms.EmailField()
	class Meta:
		model=User
		fields=['email','password1','password2']


	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address '})
		self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password '})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'})

class ProfileForm(forms.ModelForm):
	class Meta:
		model =Profile
		fields=['image',]
