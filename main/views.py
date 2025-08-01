from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class CustomLoginView(LoginView):
    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Prense Username', 'id':'inputEmail'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Prense Password', 'id':'inputPassword'})
        return form