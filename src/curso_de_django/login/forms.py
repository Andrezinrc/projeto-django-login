from django import forms
from django.contrib.auth.hashers import check_password
from register.models import Register

class LoginForm(forms.Form):
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        senha = cleaned_data.get('senha')

        if email and senha:
            try:
                user = Register.objects.get(email=email)
                if not check_password(senha, user.senha):
                    raise forms.ValidationError("Senha incorreta")
            except Register.DoesNotExist:
                raise forms.ValidationError("Usuário não encontrado")

        return cleaned_data