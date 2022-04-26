from django import forms
from django.core import validators

from budget.models import Budget, BudgetCategory


class CreateForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['description', 'category', 'actual', 'projected']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['description', 'category', 'actual', 'projected']
