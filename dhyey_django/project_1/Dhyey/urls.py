from django.contrib import admin
from django.urls import path,include

from.views import *

urlpatterns = [
    path('',School),
    path('',Schooll),
    path('post/',demos)
]
