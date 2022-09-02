from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from home.models import Recipe


class AuthorForm(forms.ModelForm):
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}),
        help_text='Obrigatório. Inserir pelo menos uma letra maiúscula e pelo menos um caractere especial',
        label='Senha',
    )

    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}),
        label='Confirme a senha',
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

        exist = User.objects.filter(username=name_user).exists()
        if exist:
            raise ValidationError(
                'Nome de usuário existente!', code='invalid'
            )

        return name_user

    def clean_email(self):
        email = self.cleaned_data.get('email')

        exist = User.objects.filter(email=email).exists()
        if exist:
            raise ValidationError('E-mail já cadastrado no banco de dados', code='invalid')
        return email

    def clean(self):
        cleaned_data = super(AuthorForm, self).clean()
        data_password = cleaned_data.get('password')
        data_password_confirm = cleaned_data.get('confirm_password')

        if data_password != data_password_confirm:
            raise ValidationError(
                {'password': 'A senha e a confirmação da senha devem ser iguais!',
                 'confirm_password': 'A senha e a confirmação da senha devem ser iguais!'}
            )

        if data_password == data_password_confirm:
            verify_char_upper = 0
            verify_char_special = 0
            error_upper = 'A senha deve ter pelo menos uma ou mais letras maiúsculas!'
            error_char_special = 'A senha deve ter pelo menos um ou mais caracteres especiais!'

            for data in data_password_confirm:
                if data.isupper():
                    verify_char_upper += 1
                if data in '@$%&*!':
                    verify_char_special += 1
            if verify_char_upper == 0 and verify_char_special == 0:
                raise ValidationError(
                    {'password': [error_upper, error_char_special],
                     'confirm_password': [error_upper, error_char_special]})
            if verify_char_upper == 0 or verify_char_special == 0:
                if verify_char_upper == 0:
                    raise ValidationError(
                        {'password': error_upper,
                         'confirm_password': error_upper}
                    )
                if verify_char_special == 0:
                    raise ValidationError(
                        {'password': error_char_special,
                         'confirm_password': error_char_special}
                    )


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'placeholder': 'senha'}))


class UserRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('author', 'title', 'description', 'time_recipe', 'image', 'order', 'step', 'recipe_category')
        widgets = {'author': forms.HiddenInput()}
