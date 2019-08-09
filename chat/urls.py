from django.urls import re_path

from . import views

urlpatterns = [
    re_path('(?P<userparameter>\d{0,10})', views.simple_chat, name='messsages'),
]