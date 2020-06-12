import requests
import os
import sys
import urllib.request
import json

from django.shortcuts import render, redirect
from .models import Movie, Genre, Actor, Director, Review

# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer

lang = 'ko-KR'
TMDB_KEY = '752946192e58cc2348b96b6bcac28ede' # -- 나중에 환경변수로 사용하자!!!

# Create your views here.
@api_view(['GET'])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

 # 1) 페이지를 돌아가면서 movies_data 받아오기 - data size => 20 x 50p (1000개)
def get_json_data(page):
    global TMDB_KEY
    global lang
    # json file 불러오기.
    json_url = f'https://api.themoviedb.org/3/discover/movie?api_key={TMDB_KEY}&language={lang}&sort_by=popularity.desc&include_adult=false&include_video=false&page={page}'
    json_data = requests.get(json_url).json()
    return json_data

# 2-0) 배우 이름 바꿔주기 | Actor name (en -> ko)
def en_to_kr(cname):
    papago_url = 'https://openapi.naver.com/v1/papago/detectLangs'
    
    # 나중에 환경변수로 설정하기!!
    client_id = "7PbRNqLKFMd89FkSeyYc" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "9AUqjaYtKA" # 개발자센터에서 발급받은 Client Secret 값

    encText = urllib.parse.quote(cname)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        trans = json.loads(response_body.decode('utf-8'))['message']['result']['translatedText']
        return trans
    else:
        print("Error Code:" + rescode)
        return

# 2) movie_obj와 Actor정보 한국어로 저장
def get_actors_and_directors(movie_id):
    global TMDB_KEY
    credit_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_KEY}&language=ko-kr'
    credit_data = requests.get(credit_URL).json()
    cast_data = credit_data['cast']
    crew_data = credit_data['crew']

    # casting
    cast_list = []
    for cast in cast_data:
        cast_list.append(en_to_kr(cast['name']))

    director_list = []
    # director
    for crew in crew_data:
        if crew['job'] == 'Director':
            director_list.append(en_to_kr(crew['name']))
    return {'cast_data':cast_list, 'directors': director_list}


from pprint import pprint as pp

def scrap(request):    
    global TMDB_KEY, lang
    page = 2
    page_limit = 2
    poster_base_url = 'https://image.tmdb.org/t/p/w500/'
    
    # Intro_준비물) Save Genre_obj & Create ko_genre_dict | id(num): name(hangul)
    ko_genres_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_KEY}&language={lang}'
    ko_genre_json_data = requests.get(ko_genres_url).json()
    ko_genres_dict = {}
    for ko_genre in ko_genre_json_data['genres']:
        g_id = ko_genre['id']
        g_name = ko_genre['name']
        ko_genres_dict[g_id] = g_name # dict로 받아서 사용

        # 장르 저장
        if Genre.objects.filter(genre_code=g_id).exists():
            continue
        else:          
            genre_obj = Genre.objects.create(genre_code=g_id, genre=g_name)
            genre_obj.save()
        

    # 실제 코드
    # 1) 페이지 돌아가면서 받아오기
    for p in range(page, page_limit+1):
        current_page_movies = get_json_data(p)['results']
        
        # 2) movie_id로 배우정보,   
        for tmp_movie in current_page_movies:
            movie_id = tmp_movie['id']
            title = tmp_movie['title']
            summary = tmp_movie['overview'],
            release_date = tmp_movie['release_date']
            poster_url = f'{poster_base_url}{tmp_movie["poster_path"]}'

            # genre, actor, director 잠시 제외
            movie_obj = Movie.objects.create(
                title = title,
                summary = summary,
                release_date = release_date,
                running_time = 20,
                poster = poster_url,
            )

            # # 이미 존재하는 영화는 추가되지 않음
            # if Movie.objects.filter(title=title, release_date=release_date).exists():
            #     pass

            # movies.genres | ManyToMany add
            genre_list = tmp_movie['genre_ids']


            for genre_num in genre_list:
                ko_genre = ko_genres_dict[genre_num]
                ko_gen_obj = Genre.objects.get(genre_code=genre_num)
                movie_obj.genres.add(ko_gen_obj)

            # movies.actors | ManyToMany add
            credit_data = get_actors_and_directors(movie_id)
            for cast_name in credit_data['cast_data']:
                if Actor.objects.filter(actor=cast_name).exists():
                    tmp_actor = Actor.objects.get(actor=cast_name)
                else:
                    tmp_actor = Actor.objects.create(actor=cast_name)
                    tmp_actor.save()
                movie_obj.actors.add(tmp_actor)

            # movies.directors | ManyToMany add
            for director_name in credit_data['directors']:
                if Director.objects.filter(director=director_name).exists():
                    tmp_director = Director.objects.get(director=director_name)
                else:
                    tmp_director = Director.objects.create(director=director_name)
                    tmp_director.save()
                movie_obj.directors.add(tmp_director)

            movie_obj.save()
    return redirect('movies:index')