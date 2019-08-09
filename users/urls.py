from django.urls import path

from . import views

urlpatterns = [
    path('userslist/', views.user_list, name='list')
]