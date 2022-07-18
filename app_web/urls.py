from django.urls import path
from .views import *

urlpatterns = [
    # path('',index,name='index'),
    path('projet/<slug>/',detail_projet,name='detail_projet'),
    path('',Contact.as_view(),name='index')
    # path('contact',Contact.as_view(),name='contact')
    # path('contact',contact,name='contact')
]