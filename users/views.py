from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import User
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from users import forms
from django.contrib import messages
from .forms import UserLoginForm
from urllib.parse import urlencode
from django.http import HttpResponse
#ПИСАТЬ ВСЁ В ACTION
# action

def index(request):
    #return render(request, 'registration/login.html')
    return render(request, 'base.html')

def main(request):
    return render(request, 'main.html')

def services(request):
    return render(request, 'services.html')

def sertificates(request):
    return render(request, 'sertificates.html')

def personalarea(request): 
    return render(request, 'personalarea.html')

def registration(request):
    return render(request, 'registration.html')




def login(request):
    form = forms.userForm()

    if request.method == "POST":
        form = forms.userForm(request.POST)
        if form.is_valid():            
            user = form.save(commit=False)
            user.login = request.POST.get("login")
            user.password = request.POST.get("password")
            user.save()   

            form = forms.userForm()      

            messages.success(request, form.Meta.success_messages['registration_success'])            

    return render(request, 'registration.html', context={'form': form})


def check_data(request):
    form = forms.UserLoginForm()    
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            login_input = cd.get("login")
            password_input = cd.get("password")
            print(password_input)
            print(login_input)
            # Используйте authenticate для аутентификации пользователя
            User = authenticate(request, username=login_input, password=password_input)

            if User is not None:
                if User.is_active:
                    login(request, User) #установка сессии 
                    messages.success(request, form.Meta.success_messages['login_success'])
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
       
              

                # form.add_error(None, 'Invalid login or password')
                # return render(request, 'login.html', context={'form': form})

    return render(request, 'login.html', context={'form': form})
#РАБОЧИЙ ВАРИК 
        # if form.is_valid():
            
        #     login_input =  (request.POST.get("login"))
        #     password_input = (request.POST.get("password"))
            
            
            
        #     try:
        #         user = User.objects.get(login=login_input, password=password_input)            
        #     except User.DoesNotExist:
        #         user = None   
        
        # if user:
        #     return render(request, 'registration/success.html')
        #     # messages.success(request, form.Meta.success_messages['login_success'])
        #     # return render(request, 'registration/success.html')
        # else:
        #     return render(request, 'registration/error.html')
#КОНЕЦ РАБОЧЕГО ВАРИКА

            # # Попытка аутентификации пользователя
            # user = authenticate(request, login=login_input, password=password_input)

            # if user is not None:
            #     # Успешная аутентификация
            #     login(request, user)
            #     query_params = urlencode({'message': 'Успешная аутентификация'})            
            #     return redirect(f'login.html?{query_params}')

            #     # form.valid_login_password = form.Meta.success_messages['login_success']
            # else:
            #     form.invalid_login = form.Meta.error_messages['invalid_login']

    
# # def check_data(request):
# #     form = forms.UserLoginForm()
# #     if request.method == "POST":
# #         form = UserLoginForm(request, data=request.POST)
# #         if form.is_valid():
# #             user = form.save(commit=False)   
# #             user.login = request.POST.get("login")
# #             user.password = request.POST.get("password")
               
# #             user = User.objects.get(user.login)    
# #             user_auth = authenticate(request, user.login, user.password)  

# #             if user_auth is not None:
# #                 login(request, user_auth)
# #                 messages.success(request, form.Meta.success_messages['registration_success'])             
# #                 # form.add_error('login', form.error_messages['invalid_login'])
# #     return render(request, 'login.html', context={'form': form})
