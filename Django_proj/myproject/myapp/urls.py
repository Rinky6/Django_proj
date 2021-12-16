from django.urls import path
from .views import *

urlpatterns = [

    path('',display),
    path('rinky/',display1),
    ]