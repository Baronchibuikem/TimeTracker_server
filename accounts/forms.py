from accounts.models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(forms.ModelForm):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ('email', 'password',)
