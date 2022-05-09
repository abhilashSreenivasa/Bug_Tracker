from django import forms
from django.core import validators
from core.models import UserProfile,Role
from bugs.models import Bug,BugType,BugPriority,BugStatus,BugHistory

bug_list= [
    ('1', 'Enhancement'),
    ('2', 'Website Content Update'),
    ('3', 'Database Update'),
    ('4', 'Change Permissions'),
    ('5', 'Bug'),
    ('6', 'UI Design Change'),
    ]

priority_list= [
    ('1', 'Low'),
    ('2', 'Medium'),
    ('3', 'High'),
    ]

class BugForm(forms.Form):
    bug_type = forms.CharField(label='Choose bug type', widget=forms.Select(choices=bug_list))
    bug_desc = forms.CharField(widget=forms.Textarea(attrs={'size': '280'}))
    bug_priority = forms.CharField(label='Choose bug priority', widget=forms.Select(choices=priority_list))



