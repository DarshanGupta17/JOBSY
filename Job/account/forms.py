from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "class":"form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {
                "class":"form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {
                "class":"forms-control"
            }
        )
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs = {
                "class":"form-control"
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = ("username","email","password1","password2","is_employer","is_jobseeker")