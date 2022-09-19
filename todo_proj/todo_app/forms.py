from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from todo_app.models import Task
from  django.forms import ModelForm

class TaskCreateForm(ModelForm):
    class Meta:
        model =Task
        fields = [
            "title",
            "description",
            "complete",
        ]
class TaskUpdateForm(ModelForm):
    class Meta:
        model =Task
        fields = [
            "title",
            "description",
            "complete",
        ]
