# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Partner

class PartnerRegisterForm(forms.ModelForm):
    username = forms.CharField(label = "", widget= forms.TextInput(attrs = {'placeholder': 'Nombre de usuario'}))
    email = forms.EmailField(label = "", widget= forms.TextInput(attrs = {'placeholder': 'Email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs = {'placeholder': 'Password'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs = {'placeholder': 'Confirmación de password'}))

    class Meta:
        model = Partner
        fields = ('username', 'email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            msg = 'Los passwords son diferentes'
            raise forms.ValidationError(msg)

        return password2

    def clean_email(self):
        data = self.cleaned_data['email']
        if Partner.objects.filter(email=data).exists():
            raise forms.ValidationError('Este email ya esta en uso')
        return data

    def save(self, commit=True):
        user = super(PartnerRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
