from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm, ForgotPassword


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class MyPasswordReset(PasswordResetView):
    email_template_name = 'email/forgot_password.html'
    form_class = ForgotPassword
    from_email = 'noahwagner035@gmail.com'
    success_url = reverse_lazy('users:password_reset_done')


from django.shortcuts import render
