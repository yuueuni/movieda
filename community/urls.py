from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_article, name='create_article'),
    path('<int:article_pk>', views.detail_article, name='detail_article'),

    path('<int:article_pk>/create_comment/', views.create_comment, name='create_comment',),
    path('<int:article_pk>/comment/<int:comment_pk>/', views.detail_comment, name='detail_comment'),
]