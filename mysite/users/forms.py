from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import CustomUser, Review
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.auth import authenticate
from django.contrib import messages

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "password"]
        error_messages = {
            'username': {
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

    
# # class UserLoginForm(AuthenticationForm):
class UserLoginForm(forms.Form):   
    class Meta:
        model = CustomUser
        fields = ["username", "password"]
        error_messages = {  
            'invalid_login_password':'Неправильный логин/пароль123',              
        }
    
 # username = forms.CharField()
    # password = forms.CharField()
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get("username")
    #     password = cleaned_data.get("password")

        # Вы можете добавить дополнительную валидацию здесь, если необходимо

        # return cleaned_data

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['stars', 'comment', 'image']
        
