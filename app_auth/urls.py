from django.urls import path
from .views import *

urlpatterns = [
    path('register',register,name='register'),
    path('login',login,name='_login'),
    path('logout',logout,name='_logout'),
]