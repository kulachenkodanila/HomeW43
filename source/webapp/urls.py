from django.contrib import admin
from django.urls import path

from webapp.views import home_work

urlpatterns = [
    path("", home_work),

]
