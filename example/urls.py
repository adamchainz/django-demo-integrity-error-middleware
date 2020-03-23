from django.urls import path

from example.core.views import index


urlpatterns = [
    path("", index),
]
