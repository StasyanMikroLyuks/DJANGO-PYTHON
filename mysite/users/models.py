from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_user(self, username,  password=None):
        
        user = self.model(
            username=username,            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,  password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username=username,
            password=password,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # email = models.EmailField(
    #     verbose_name="email address",
    #     max_length=255,
    #     unique=True,
    # )

    username = models.CharField("Имя пользователя", unique=True, max_length=255)
    
    # password = models.CharField("Пароль", max_length=255)
   
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def __str__(self):
        return self.username
    

#КЛАСС ДЛЯ ОТЗЫВОВ
class Review(models.Model):
    stars = models.IntegerField()
    comment = models.TextField()
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.FileField(blank=True)
    # image = models.ImageField(upload_to='reviews/', height_field=None, width_field=None, max_length=100, default='static/media/reviews/default_image.jpg')
    def __str__(self):
        return f"{self.user.username} - {self.stars} stars"

class ReviewImage(models.Model):
    post = models.ForeignKey(Review, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reviews/', height_field=None, width_field=None, max_length=100, default='static/media/reviews/default_image.jpg')

    def __str__(self):
        return f"{self.post.user.username} - {self.post.stars} stars"

# КЛАСС ДЛЯ СОТРУДНИКОВ
class Person(models.Model):
    name = models.TextField()
    job_title = models.TextField()
    bio = models.TextField()
    image = models.ImageField(upload_to='card/', height_field=None, width_field=None, max_length=100)
    

# Класс для товаров
class Product(models.Model):    
    name = models.CharField(max_length=200, db_index=True)   #название
    image = models.ImageField(upload_to='products/', blank=True) #картинка
    description = models.TextField(blank=True) #описание
    price = models.DecimalField(max_digits=10, decimal_places=2) #цена
    stock = models.PositiveIntegerField() # Это поле PositiveIntegerField для хранения остатков данного продукта.
    available = models.BooleanField(default=True) #доступен/не доступен
    

#модель свечи для графика
class Candle(models.Model):
    open_price = models.FloatField() #Цена открытия свечи.
    close_price = models.FloatField() #Цена закрытия свечи
    high_price = models.FloatField() #Максимальная цена в течение периода свечи.
    low_price = models.FloatField() #Минимальная цена в течение периода свечи.
    volume = models.FloatField() #Объем свечи
    timestamp = models.DateTimeField() #timestamp: Временная метка свечи

    def __str__(self):
        return f'Candle {self.timestamp}'