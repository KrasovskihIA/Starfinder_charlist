from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField 
from django.contrib.auth.models import User

# Форма для входа на аккаунт
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'placeholder': 'Username',
        'class': 'form-control'
    }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'placeholder': 'Пароль',
        'class': 'form-control'
    }))

    error_messages = {
        'invalid_login': 'Введен неверный пароль'
    }

# Форма для регистрации
class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label= 'Пароль',
        widget= forms.widgets.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'class': 'form-control'
        }))

    password2 = forms.CharField(
        label = 'Повторите пароль',
        widget = forms.widgets.PasswordInput(attrs={
            'placeholder': 'Повторите пароль',
            'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('email', 'username')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Email'})
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=User).exists():
            raise forms.ValidationError('Email addresses must be unique')
        return email
