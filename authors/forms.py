from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class AuthorForm(forms.ModelForm):
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}),
        label='Senha',
        error_messages={'required': 'password must not be empty'}
    )

    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}),
        label='Confirme a senha',
        error_messages={'required': 'Campo obrigatório!'}
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

        labels = {
            'username': 'Nome de usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
            'username': forms.TextInput(attrs={'placeholder': 'Nome de usuário'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
        }

    # Validação de um campo especifico
    def clean_username(self):
        name_user = self.cleaned_data.get('username')

        if 'F1' in name_user:
            raise ValidationError(
                'Nome de usuário inválido!'
            )

        return name_user

    def clean(self):
        cleaned_data = super(AuthorForm, self).clean()
        data_password = cleaned_data.get('password')
        data_password_confirm = cleaned_data.get('confirm_password')

        if data_password != data_password_confirm:
            raise ValidationError(
                {'password': 'A senha e a confirmação da senha devem ser iguais!',
                 'confirm_password': 'A senha e a confirmação da senha devem ser iguais!'}
            )

