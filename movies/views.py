import requests
import os
import sys
import urllib.request
import json

from django.shortcuts import render
from .models import Movie, Genre, Actor, Director, Review

# Create your views here.
class scrap(request):
    lang = 'ko-KR'
    TMDB_KEY = 'f790c6911bd5abe1dd9098d76849459f' # -- 나중에 환경변수로 사용하자!!!
    page = 1
    page_limit = 50
    discover_url = f'https://api.themoviedb.org/3/discover/movie?api_key={TMDB_KEY}&language={lang}&sort_by=popularity.desc&include_adult=false&include_video=false&page={page}'
    poster_base_url = 'https://image.tmdb.org/t/p/w500/'
    
    # Intro_준비물) Save Genre_obj & Create ko_genre_dict | id(num): name(hangul)
    ko_genres_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_KEY}&language={lang}'
    ko_genre_json_data = requests.get(ko_genres_url).json()
    ko_gernes_dict = {}
    for ko_genre in ko_genre_json_data['genres']:
        g_id = ko_genre['id']
        g_name = ko_genre['name']
        ko_genre_dict['g_id'] = g_name # dict로 받아서 사용
        if Genre.objects.filter(genre=g_name).exists():
            continue
        else:
            Genre.objects.create(genre=g_name)

    # 1) 페이지를 돌아가면서 movies_data 받아오기 - data size => 20 x 50p (1000개)
    def get_json_data(page):
        global TMDB_KEY
        global lang
        # json file 불러오기.
        json_url = f'https://api.themoviedb.org/3/discover/movie?api_key={TMDB_KEY}&language={lang}&sort_by=popularity.desc&include_adult=false&include_video=false&page={page}'
        json_data = reqeust.get(json_url).json()
        return json_data

    # 2-0) 배우 이름 바꿔주기 | Actor name (en -> ko)
    def en_to_kr(cname):
        papago_url = 'https://openapi.naver.com/v1/papago/detectLangs'
        
        # 나중에 환경변수로 설정하기!!
        client_id = "DnpIALAz5nZRI_RUU4O_" # 개발자센터에서 발급받은 Client ID 값
        client_secret = "Kp1APx_Zt8" # 개발자센터에서 발급받은 Client Secret 값

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


    # 실제 코드
    # 1) 페이지 돌아가면서 받아오기
    for p in range(page, page_limit+1):
        current_movies = get_json_data(p)['results']

        # 2) movie_id로 배우정보,   
        for tmp_movie in current_movies:
            movie_id = tmp_movie['id']
            title = tmp_movie['title']
            summary = tmp_movie['overview']
            running_time = tmp_movie['runtime']
            release_date = tmp_movie['release_date']
            poster_url = f'{poster_base_url}{tmp_movie["poster_path"]}'

    
    for tmp_movie in movies:
        title = tmp_movie['title']
        summary = tmp_movie['overview']
        running_time = tmp_movie['runtime']
        release_date = tmp_movie['release_date']
        poster_url = f'{poster_base_url}{tmp_movie["poster_path"]}'
        
        # 이미 존재하는 영화는 추가되지 않음
        if Movie.objects.filter(title=title, release_date=release_date).exists():
            continue
        
        # genre, actor, director 잠시 제외
        movie_obj = Movie.objects.create(
            title = title
            summary = summary
            release_date = release_date
            running_time = running_time
            poster = poster_url
        )

        # 장르 ManyToMany 추가
        genres = tmp_movie['genres']
        for genre_num in genres:
            ko_genre = hangul_genres[genre_num]
            movie_obj.genres

    return redirect('index')