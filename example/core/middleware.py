from django.db.utils import IntegrityError
from django.http import HttpResponse


class IntegrityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if isinstance(exception, IntegrityError):
            return HttpResponse("😨 IntegrityError")
