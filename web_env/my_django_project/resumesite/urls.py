from django.contrib import admin
from django.urls import include, re_path
from . import views


urlpatterns = [
    re_path('', views.home, name="home"),
]
