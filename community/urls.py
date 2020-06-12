from django.contrib import admin
from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_article, name='create_article'),
    path('<int:article_pk>/', views.detail_article, name='detail_article')
]