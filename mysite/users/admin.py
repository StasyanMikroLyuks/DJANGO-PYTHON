from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users import models
from users.models import Review, ReviewImage, Person, Product


class CustomUserAdmin(UserAdmin):
    """Регистрация модели CustomUser в админ панели"""
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('username',)}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    list_display = ('__str__', 'username',)

    list_filter = ('username',)

    search_fields = ('username',)

    ordering = ('username',)

    add_fieldsets = (
        ("User Details", {'fields': ('username', 'username', 'password1', 'password2')}),
    )

admin.site.register(models.CustomUser, CustomUserAdmin)

#админ панель для сотрудников
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'bio', 'image')

admin.site.register(Person, PersonAdmin)


#админ панель для товаров
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'price', 'stock', 'available')

admin.site.register(Product, ProductAdmin)


#ReviewImageInline, ReviewAdmin, ReviewImageAdmin - АДМИН ПАНЕЛЬ ДЛЯ ОТЗЫВОВ. 
class ReviewImageInline(admin.TabularInline):  # Используйте TabularInline или StackedInline в зависимости от предпочтений по отображению
    model = ReviewImage 
    extra = 1

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'stars', 'timestamp')
    #list_display определяет, какие поля будут отображаться в списке записей. 
    search_fields = ('user__username', 'stars')
    #search_fields добавляет возможность поиска записей по указанным полям. 
    list_filter = ('stars',)
    #list_filter добавляет фильтр по звёздам для удобства. 
    inlines = [ReviewImageInline]
    #добавляет встроенную форму для изображений в админ-панели отзывов

class ReviewImageAdmin(admin.ModelAdmin):
    list_display = ('post_user', 'post_stars', 'image')
    #list_display определяет, какие поля будут отображаться в списке записей.
    search_fields = ('post__user__username', 'post__stars')
    #search_fields добавляет возможность поиска записей по указанным полям.

    def post_user(self, obj):
        return obj.post.user.username

    def post_stars(self, obj):
        return obj.post.stars

    post_user.short_description = 'User'
    post_stars.short_description = 'Stars'

    #post_user и post_stars - это методы для отображения имени пользователя 
    # и количества звезд в списке изображений. 
    # short_description используется для установки пользовательских заголовков для этих полей.

admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewImage, ReviewImageAdmin)

#Эти строки регистрируют модели и соответствующие классы администратора в админ-панели Django, 
# чтобы они стали доступными для управления через интерфейс администратора.
