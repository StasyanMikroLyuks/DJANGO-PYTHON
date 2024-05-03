from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser, Review, ReviewImage, Person, Product, Candle
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from users import forms
from django.contrib import messages
from .forms import UserLoginForm, ReviewForm
from django.utils import timezone
from urllib.parse import urlencode
from django.http import HttpResponse
import pdb
import os
import logging
from django.conf import settings
from django.core.files.storage import default_storage
import requests
from datetime import datetime
#ПИСАТЬ ВСЁ В ACTION
# action

def index(request):
    #return render(request, 'registration/login.html')
    return render(request, 'base.html')

def main(request):
    persons = Person.objects.all()
    return render(request, 'main.html', {'persons': persons})
    # return render(request, 'main.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})    

def services(request):
    return render(request, 'services.html')

def sertificates(request):
    return render(request, 'sertificates.html')

def personalarea(request):
    return render(request, 'personalarea.html')

def registration(request):
    return render(request, 'registration.html')

def authorization(request):
    return render(request, 'authorization.html')

def reviews(request):
    return render(request, 'reviews.html')

def cabinet(request):
    return render(request, 'cabinet.html')

def graph(request):
    return render(request, 'graph.html')

def register(request):
    form = forms.UserForm()

    if request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = request.POST.get("username")
            user.password = request.POST.get("password")

            existing_User = CustomUser.objects.filter(username=request.POST.get("username")).exists()
            if existing_User == True:
                messages.error(request, form.Meta.error_messages['required'])
                # return render(request, 'registration.html', context={'error': "Пользователь уже существует" })
            else:
                CustomUser.objects.create_user(request.POST.get("username"),request.POST.get("password"))
                messages.success(request, form.Meta.success_messages['registration_success'])
                return render(request, 'authorization.html')

                # user_registered = True  # Устанавливаем флаг успешной регистрации
            # if existing_User == False:
            #     return render(request, 'registration.html', context={'error': "Пользователь зарегистрирован" })

    return render(request, 'registration.html', context={'form': form})
#'user_registered': user_registered


def check_data(request):
    form = UserLoginForm()
    print('1233213',request.method)
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        print('5555', form.is_valid())
        if form.is_valid():           
            username = request.POST.get('username')
            password = request.POST.get('password')
                        
            user = authenticate(request, username=username, password=password)            
            # print('user', user.is_active)
            if user is not None and user.is_active:                            
                    messages.success(request, 'Вы успешно авторизованы.')                    
                    login(request, user) 
            else:
                # messages.error(request, 'Неправильный логин/пароль.') 
                messages.error(request, form.Meta.error_messages['invalid_login_password'])  

                            
    return render(request, 'authorization.html', context={'form': form})     

            # if not authenticate(request, username=username, password=password):
            #         print('adsada')
            #         messages.error(request, 'Неправильный логин или пароль.')
                    
                                                        
            # else:
            #     existing_user = CustomUser.objects.filter(username=request.POST.get("username")).exists()
            #     if not existing_user:
            #         messages.error(request, 'Неправильный логин.')
            #         print('jhkhjkhjkhkjs')
            #     else:
            #         if not authenticate(request, username=username, password=password):
            #             messages.error(request, 'Неправильный логин или пароль.')
                    

                # messages.error(request, 'Неправильный логин или пароль.')
                # print('jhkhjkhjkhkjs')
                # return render(request, 'main.html')
    

def logout_user(request): #выход из авторизованного пользователя
    logout(request)
    return render(request, 'main.html')  


def make_reviews(request):  
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            print('1233213',request.method)
            stars = request.POST.get('stars')
            comment = request.POST.get('comment')
            # image = request.FILES.get('image')
            image = request.FILES.getlist('image')  # Получаем список изображений
            
            user = request.user if request.user.is_authenticated else None
            current_datetime = timezone.now()

            if not comment.strip():
                messages.error(request, 'Комментарий не может быть пустым.')
            else:
                review = Review(stars=stars, comment=comment, user=user, timestamp=current_datetime)
                review.save()

                for image in image:
                    post_image = ReviewImage(post=review, image=image)
                    post_image.save()
        else:
            form = ReviewForm()   

    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews':reviews}  )

def fetch_and_save_candles():
    # Замените URL на ваш онлайн-график
    url = 'https://chat.openai.com/c/af8c55c4-82cd-4ec8-85a1-6c46ec5ddf48'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        for candle_data in data:
            timestamp = datetime.fromtimestamp(candle_data['timestamp'])
            candle = Candle.objects.create(
                open_price=candle_data['open'],
                close_price=candle_data['close'],
                high_price=candle_data['high'],
                low_price=candle_data['low'],
                volume=candle_data['volume'],
                timestamp=timestamp,
            )
            
            candle.save()

# Вызовите эту функцию при необходимости обновления данных
fetch_and_save_candles()