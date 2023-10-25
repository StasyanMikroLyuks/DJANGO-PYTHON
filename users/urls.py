from django.urls import path, include
from users import views
from .views import index

urlpatterns = [
    path('', views.main, name='home'), 
    path('main', views.main, name='main'),
    path('services', views.services, name='services'),
    path('sertificates', views.sertificates, name='sertificates'),
    path('personalarea', views.personalarea, name='personalarea'),
    path('registration', views.registration, name='registration'),    
    
    path('login', views.login, name='login'),
    path('check_data', views.check_data, name='check_data'),

    #views. ... где ... название функции с views.py
    
    # ,
]