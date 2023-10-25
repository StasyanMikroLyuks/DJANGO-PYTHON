from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    login = models.CharField("Логин", max_length=100, unique=True)
    password = models.CharField("Пароль", max_length=100)
