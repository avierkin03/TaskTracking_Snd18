from django import forms
from .models import Task

# Форма для фільтра задач
class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ("", "All"),
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done")
    ]

    PRIORITY_CHOICES = [
        ("", "All"),
        ("low", "Low"),
        ("medium", "Medium"),
        ("hight", "Hight")
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, label="Status", required=False)
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, label="Priority", required=False)

    def __init__(self, *args, **kwargs):
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        self.fields["status"].widget.attrs.update({"class": "form-control"})
        self.fields["priority"].widget.attrs.update({"class": "form-control"})


# Форма для створення задач
class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "deadline", "owner"]
    
    def __init__(self, *args, **kwargs):
        super(TaskCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
        self.fields["deadline"].widget.attrs["class"] += " my-custom=datepicker"