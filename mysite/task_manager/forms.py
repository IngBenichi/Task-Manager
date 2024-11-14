# task_manager/forms.py

from django import forms
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'due_date', 'priority', 'tags']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'project', 'due_date', 'priority', 'tags', 'parent_task']
