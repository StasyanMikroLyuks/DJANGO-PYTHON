from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User
from django.core.exceptions import NON_FIELD_ERRORS


class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["login", "password"]
        error_messages = {
            'login': {
                'unique': "Пользователь с таким логином уже зарегистрирован",
                'required': "Поле 'Логин' должно быть заполнено.",

            },
            'password': {
                'required': "Поле 'Пароль' должно быть заполнено.",
            },
        }
        success_messages = {
            'registration_success': 'Пользователь успешно зарегистрирован.'
        }
    
class UserLoginForm(AuthenticationForm):    
    class Meta:
        model = User
        fields = ["login", "password"]
        error_messages = {
            'invalid_login': 'Пользователя с таким логином не существует',
            'invalid_password': 'Неправильный пароль.',
        }
        success_messages = {
            'login_success': 'Пользователь успешно авторизован.'
        }
