from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

app_name = 'category'

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('add/', views.addCategory, name="add_category"),
]
