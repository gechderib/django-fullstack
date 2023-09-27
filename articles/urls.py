from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('<str:slug>/', views.article_detail)
]
