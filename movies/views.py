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

from decouple import config

lang = 'ko-KR'
TMDB_KEY = config("TMDB_KEY")


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

    client_id = config("CLIENT_ID")
    client_secret = config("CLIENT_SECRET")

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

# 2) Actor & Director 불러오기
def get_actors_and_directors(movie_id, original_title):
    client_id = config("CLIENT_ID")
    client_secret = config("CLIENT_SECRET")

    encText = urllib.parse.quote(original_title)
    url = f"https://openapi.naver.com/v1/search/movie?query={encText}&display=1" # json 결과

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    
    if(rescode==200):
        response_body = response.read()
        trans = json.loads(response_body.decode('utf-8'))['items']
        # 만약 검색결과가 있는 경우
        if trans:
            actor_list = trans[0]['actor'].split('|')[:-1]
            director_list =  trans[0]['director'].split('|')[:-1]
            return {'actor_list': actor_list, 'director_list':director_list}
        
        # 없는 경우에만 movie_detail.credit 정보를 파파고로 번역
        else:
            # 1) movie_detail.credits에서 정보 불러오기
            global TMDB_KEY
            credit_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_KEY}&language=ko-kr'
            credit_data = requests.get(credit_URL).json()
            cast_data = credit_data['cast']
            crew_data = credit_data['crew']

            # 2) papago로 번역후 return
            # actors
            actor_list = []
            for cast in cast_data:
                actor_list.append(en_to_kr(cast['name']))

            director_list = []
            # director
            for crew in crew_data:
                if crew['job'] == 'Director':
                    director_list.append(en_to_kr(crew['name']))
            return {'actor_list':actor_list, 'director_list': director_list}

    else:
        print("Error Code:" + rescode)
        return

def get_runningtime(movie_id):
    global TMDB_KEY
    movie_detail_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_KEY}'
    movie_detail_data = requests.get(movie_detail_url).json()
    running_time = movie_detail_data['runtime']
    return running_time
    
def scrap(request):    
    global TMDB_KEY, lang
    page = 1
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
        
        # 2) movie를 순회하며 저장
        for tmp_movie in current_page_movies:
            movie_id = tmp_movie['id']
            title = tmp_movie['title']
            summary = tmp_movie['overview'],
            release_date = tmp_movie['release_date']
            poster_url = f'{poster_base_url}{tmp_movie["poster_path"]}'
            
            # movie_detail => running_time 받아오기
            running_time = get_runningtime(movie_id)

            # genre, actor, director 잠시 제외
            movie_obj = Movie.objects.create(
                title = title,
                summary = summary,
                release_date = release_date,
                running_time = running_time,
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

            # original_title => naver_search_api를 이용하여 get_actor_and_director로 넘기기,   
            original_title = tmp_movie['original_title']
            credit_data = get_actors_and_directors(movie_id, original_title)
            for cast_name in credit_data['actor_list']:
                if Actor.objects.filter(actor=cast_name).exists():
                    tmp_actor = Actor.objects.get(actor=cast_name)
                else:
                    tmp_actor = Actor.objects.create(actor=cast_name)
                    tmp_actor.save()
                movie_obj.actors.add(tmp_actor)

            # movies.directors | ManyToMany add
            for director_name in credit_data['director_list']:
                if Director.objects.filter(director=director_name).exists():
                    tmp_director = Director.objects.get(director=director_name)
                else:
                    tmp_director = Director.objects.create(director=director_name)
                    tmp_director.save()
                movie_obj.directors.add(tmp_director)

            movie_obj.save()
    return redirect('movies:index')
