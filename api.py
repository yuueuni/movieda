from pprint import pprint as pp

# # 1. 영화진흥위원회 api

# URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=6a6147c0832886a864adffc90f8afee1' 

# json_data = requests.get(URL).json()


# movies = []
# for i in json_data['movieListResult']['movieList']:
#     getMovieCd = i['movieCd']
#     movies.append(getMovieCd)


# detail_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=430156241533f1d058c603178cc3ca0e&movieCd=' + movies[0]
# peopleUrl = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key=430156241533f1d058c603178cc3ca0e&peopleNm=Chris Hemsworth'
# movie_data = requests.get(peopleUrl).json()
# # pp(movie_data)

# mylist = list(''.join(movie_data['peopleListResult']['peopleList'][0]['filmoNames']).split('|'))
# print(mylist)

# import requests

# tmdbUrl = 'https://api.themoviedb.org/3/movie/299536/credits?api_key=f790c6911bd5abe1dd9098d76849459f&language=ko-kr'
# castData = requests.get(tmdbUrl).json()

# cname = castData['cast'][0]['name']

# # papago

# papago_url = 'https://openapi.naver.com/v1/papago/detectLangs'
# client_id = 'DnpIALAz5nZRI_RUU4O_'
# clitent_secret = 'Kp1APx_Zt8'

# import os
# import sys
# import urllib.request
# import json

# client_id = "DnpIALAz5nZRI_RUU4O_"
# client_secret = "Kp1APx_Zt8"

# encText = urllib.parse.quote(cname)
# data = "source=en&target=ko&text=" + encText

# url = "https://openapi.naver.com/v1/papago/n2mt"

# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request, data=data.encode("utf-8"))
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     trans = json.loads(response_body.decode('utf-8'))['message']['result']['translatedText']
#     print(trans)
# else:
#     print("Error Code:" + rescode)


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