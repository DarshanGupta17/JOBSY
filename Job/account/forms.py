from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib import messages

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
                "class":"form-control"
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

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        email = cleaned_data.get("email")
        username = cleaned_data.get("username")
        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords don't match")
        if CustomUser.objects.filter(email = email).exists():
            self.add_error('email',"email already exits")
        if CustomUser.objects.filter(username = username).exists():
            self.add_error('username',"username already exits")
        return cleaned_data