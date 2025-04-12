from django import forms
from .models import Task

class CSVImportForm(forms.Form):
    file = forms.FileField()


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'category', 'completed', 'parent_task']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    # Display only tasks that are not subtasks (tasks with no parent)
    parent_task = forms.ModelChoiceField(
        queryset=Task.objects.filter(parent_task__isnull=True),
        required=False,
        empty_label="None (This is a main task)"
    )


