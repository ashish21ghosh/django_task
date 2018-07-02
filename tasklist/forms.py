from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# class DateInput(forms.DateInput):
#     input_type = 'date'

class TaskForm(forms.ModelForm):
    # """docstring for TaskForm"""
    task_head = forms.CharField(label='Your Task', max_length=200, help_text='Required')

    class Meta:
        model = Task
        widgets = {
            'task_head': forms.TextInput(attrs={'class': "form-control", }),
            'description': forms.Textarea(attrs={'rows': 5, 'class': "form-control", }),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': "form-control", }),
            'parent_task': forms.TextInput(attrs={'class': "form-control", }),
            'task_group': forms.HiddenInput(),
        }
        fields = ('task_head', 'description', 'due_date', 'parent_task', 'task_group')
    # widgets = {
     #        'due_date': DateInput(),
     #    }
    parent_task = forms.CharField(label='Parent Task', max_length=15, required=False)
    

