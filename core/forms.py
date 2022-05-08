from django import forms
from django.core import validators
from core.models import UserProfile,Role
from django.contrib.auth.models import User


#role_list=Role.objects.values('role')
role_list= [
    ('2', 'Manager'),
    ('3', 'Developer'),
    ('4', 'Client'),
    ]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class JoinForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'size': '30'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'size': '30'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    role= forms.CharField(label='Choose your role', widget=forms.Select(choices=role_list))

    """  class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        help_texts = {
            'username': None       }
    """