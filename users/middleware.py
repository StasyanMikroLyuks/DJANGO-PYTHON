#для того чтоб появлялось окно пользователя на сайте
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class UserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_id = request.session.get('user_id')
        request.user = None

        if user_id:
            try:
                request.user = User.objects.get(id=user_id)
            except ObjectDoesNotExist:
                pass

        response = self.get_response(request)
        return response