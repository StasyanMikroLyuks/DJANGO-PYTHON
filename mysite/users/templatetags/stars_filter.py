from django import template

register = template.Library()

@register.filter(name='stars_display')
def stars_display(value):
    try:
        stars = int(value)
    except ValueError:
        stars = 0  # Или любое другое значение по умолчанию для обработки ошибки
    filled_stars = '★' * stars
    empty_stars = '☆' * (5 - stars)
    return f"{filled_stars}{empty_stars}"