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

status_list=[

    ('1','New'),
    ('2','Open'),
    ('3', 'In Progress'),
    ('4', 'Closed'),
    ('5', 'Cancelled'),
    
]
staff_list=[]
for x in UserProfile.objects.all():
    if x.role.role_id=='2' or x.role.role_id=='3':
        staff_list.append((x.id,x.username))


class BugForm(forms.Form):
    bug_type = forms.CharField(label='Choose bug type', widget=forms.Select(choices=bug_list))
    bug_desc = forms.CharField(widget=forms.Textarea(attrs={'size': '280'}))
    bug_priority = forms.CharField(label='Choose bug priority', widget=forms.Select(choices=priority_list))


class UpdateForm(forms.Form):
    bug_type = forms.CharField(label='Change bug type', widget=forms.Select(choices=bug_list))
    bug_desc = forms.CharField(widget=forms.Textarea(attrs={'size': '280'}))
    bug_priority = forms.CharField(label='Change bug priority', widget=forms.Select(choices=priority_list))
    bug_status = forms.CharField(label='Change bug status', widget=forms.Select(choices=status_list))

class AssignForm(forms.Form):
    bug_owner = forms.CharField(label='Assign the ticket', widget=forms.Select(choices=staff_list))





