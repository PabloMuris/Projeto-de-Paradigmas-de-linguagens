from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'idade', 'curso']
        widgets = {
            'nome': forms.TextInput(attrs={'id': 'nome'}),
            'idade': forms.NumberInput(attrs={'id': 'idade', 'min': 0}),
            'curso': forms.Select(attrs={'id': 'curso'}),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'id': 'nome'}),
        }
