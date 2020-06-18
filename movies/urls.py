from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.index, name="index"),
    path('scrap/<int:page>/<int:page_count>/', views.scrap, name="scrap"),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('search/', views.search, name="search"),
    
    path('<int:movie_pk>/', views.movie_detail, name="movie_detail"),
    path('like_movie/<int:movie_pk>', views.like_movie, name="like_movie"),

    path('<int:movie_pk>/get_review/', views.get_review, name='get_review'),
    path('<int:movie_pk>/create_review/', views.create_review, name='create_review'),
    path('<int:movie_pk>/delete_review/<int:review_pk>', views.delete_review, name='delete_review'),
]