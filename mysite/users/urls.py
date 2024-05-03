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
    path('authorization', views.authorization, name='authorization'),
    path('reviews', views.reviews, name='reviews'),
    path('cabinet', views.cabinet, name='cabinet'),
    path('graph', views.graph, name='graph'),
    path('shop', views.shop, name='shop'),

    path('register', views.register, name='register'),
    path('check_data', views.check_data, name='check_data'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('make_reviews', views.make_reviews, name='make_reviews'),
    #views. ... где ... название функции с views.py
    path('stock_data_json', views.fetch_and_save_candles, name='stock_data_json')
    # ,
]