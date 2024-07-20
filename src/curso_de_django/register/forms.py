from django.contrib.auth.hashers import make_password
from django import forms
from .models import Register

class RegisterForm(forms.ModelForm):
    confirma_senha = forms.CharField(max_length=128, widget=forms.PasswordInput())

    class Meta:
        model = Register
        fields = ['nome', 'email', 'senha']
        widgets = {
            'senha': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirma_senha = cleaned_data.get("confirma_senha")

        if senha and confirma_senha and senha != confirma_senha:
            self.add_error('confirma_senha', "As senhas não coincidem")

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.senha = make_password(self.cleaned_data['senha'])
        if commit:
            instance.save()
        return instance