"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

# -*- coding: utf-8 -*-
from django import forms
class BookForm(forms.Form):
    title = forms.CharField(max_length=30, required=True, label='Podaj tytul ksiazki', error_messages={'required': 'Wpisz jakas wartosc!!','max_length': 'Za dlugi wpis!!!'})
    about = forms.CharField(required=True, widget=forms.Textarea, label='Podaj opis ksiazki', error_messages={'required': 'Wpisz jaks wartosc!!'})
    timestamp = forms.CharField(max_length=4, required=True, label='Podaj rok napisania ksiazki', error_messages={'required': 'Wpisz jaks wartosc!!'})

#komentarze do ksiazki
class CommentForm(forms.Form):
    body = forms.CharField(label='Wpisz komentarz', required=True, error_messages={'required': 'Wpisano pusty komentarz!'})