from django.contrib import admin
from django.urls import path,include

from.views import *

urlpatterns = [
    path('',School),
    # path('get/',Schooll),
    path('post/',post),
    path('put/<id>/',putt),
    path('patch/<id>/',patchh),
    path('delete/<id>/',deletee)
]
