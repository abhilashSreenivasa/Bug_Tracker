from django import forms
from django.core import validators
from tasks.models import Task, TaskCategory


class CreateForm(forms.Form):
    name = forms.CharField(min_length=1, strip=True,
                           label="Desctiption",
                           validators=[validators.MinLengthValidator(1)],
                           widget=forms.TextInput(
                               attrs={"size": "30"}))
    category = forms.ModelChoiceField(queryset=TaskCategory.objects.all())

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'category']
