import requests
import os
import sys
import urllib.request
import json

api_key = 'f790c6911bd5abe1dd9098d76849459f'

tmdbUrl = 'https://api.themoviedb.org/3/movie/299536/credits?api_key=f790c6911bd5abe1dd9098d76849459f&language=ko-kr'
castData = requests.get(tmdbUrl).json()
cname = castData['cast'][0]['name']

def get_actors_data(movie_id):
    global api_key
    cast_list = []
    cast_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=ko-kr'
    cast_data = requests.get(cast_URL).json()
    for c_data in cast_data['cast']:
        cast_list.append(c_data['name'])
    return cast_list

def en_to_kr(cname):
    papago_url = 'https://openapi.naver.com/v1/papago/detectLangs'
    client_id = 'DnpIALAz5nZRI_RUU4O_'
    clitent_secret = 'Kp1APx_Zt8'

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
        return trans.encode("utf-8")
    else:
        print("Error Code:" + rescode)
        return

movie_id = 299536
cast_list = get_actors_data(movie_id)

for cname in cast_list:
    print(en_to_kr(cname))