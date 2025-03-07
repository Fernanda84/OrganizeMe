from django import forms
import re
from .models import Atividade, UserCostumizado, Perfil
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


class CadastroForm(forms.ModelForm):
    username = forms.CharField(
        min_length=4,
        max_length=30,
        label="Usuário:",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text="O nome de usuário deve ter entre 4 e 30 caracteres e pode conter letras, números e _. "
    )
    
    email = forms.EmailField(
        label="Email:",
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        help_text="Informe um email válido."
    )

    password1 = forms.CharField(
        label="Senha:",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8,
        help_text="A senha deve ter pelo menos 8 caracteres, incluindo uma letra maiúscula, uma minúscula e um número."
    )

    password2 = forms.CharField(
        label="Confirme a senha:",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = UserCostumizado
        fields = ['username', 'email', 'password1', 'password2']

    
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuário:",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Senha:",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class EditarPerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ['cidade', 'estado', 'data_nascimento', 'telefone', 'avatar']
        widgets = {
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
        }

    


class AlterarSenhaForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Senha atual:",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['materia', 'conteudo', 'status', 'prazo']
