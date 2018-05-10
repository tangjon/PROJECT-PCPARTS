from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UsernameField

from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.forms import ModelForm

from account.models import UserProfile


class SignUpForm(UserCreationForm):
    # email1 = forms.EmailField(
    #     label="Email",
    #     help_text="Email Address",
    # )
    # email2 = forms.EmailField(
    #     label="Email Confirmation",
    #     help_text="Enter the same email as before, for verification.",
    # )

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password1', 'password2']
    #
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user
