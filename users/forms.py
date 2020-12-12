from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'subscription', 'user_cell_phone')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'subscription', 'user_cell_phone')


class ForgotPassword(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs=
                                                     {'class': 'form-control', 'title': 'Enter Email',
                                                      'placeholder': 'Email'}),
                             max_length=50, label=False, required=True,
                             )
