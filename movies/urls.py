from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.index, name="index"),
    path('scrap/', views.scrap, name="scrap"),
    path('search/', views.search, name="search"),

    path('like_actor/<int:actor_pk>/', views.like_actor, name="like_actor"),
    path('like_director/<int:director_pk>/', views.like_director, name="like_director"),
    path('like_movie/<int:movie_pk>/', views.like_movie, name="like_movie"),

    path('<int:movie_pk>/get_review/', views.get_review, name='get_review'),
    path('<int:movie_pk>/create_review/', views.create_review, name='create_review'),
    path('<int:movie_pk>/delete_review/<int:review_pk>', views.delete_review, name='delete_review'),
]