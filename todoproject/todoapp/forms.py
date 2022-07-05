from pyexpat import model
from django.forms import ModelForm
from .models import todomodel

class TodoForm(ModelForm):
    class Meta:
        model = todomodel
        fields = ['title', 'memo', 'important']