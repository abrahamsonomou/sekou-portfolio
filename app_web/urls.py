from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('cv',cv,name='cv'),
    path('projet/<int:pk>/',detail_projet,name='detail_projet'),
    path('contact',contact,name='contact')
]