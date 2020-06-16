# Final Project

## 목표
- 영화 정보 기반 추천 서비스
- 커뮤니티

## 개발 환경
- Django 2.1.15
- Python 3.7+

- Node 12.18.X
- Vue 2.6+

- Django REST API 서버 & Vue.js

- SQLite
- AWS 배포

## 프로젝트 기간
- 2020.06.11(목) - 2020.06.16(화)
- 발표 준비 : 2020.06.17(수)

- 발표 : 2020.06.19(금)


## 서비스 개요
1. 영화 데이터 수집 - The Movie Database(TMDb)
    - 데이터 50개 이상
2. 반응형 웹
    - README.md 프로젝트 구조 명시 필수
3. 영화 커뮤니티 기능
4. 영화 추천 서비스 (알아서 구현) - 방법 추후
5. 디자인 및 배포 (+유지보수)

### 필수 기능
- 관리자
    - 영화 CRUD
    - 유저 관리
- 영화 정보
  
    - 유저 영화 평점 등록,수정,삭제
- 추천 알고리즘
  
    - 등록한 평점 기반 영화 추천
- 커뮤니티(영화 관련 정보)
    - 게시글, 댓글 CRUD (생성, 수정 시간 표기)
    - 게시글 pagination

    + 복수의 기능 게시판, 권한 나누어 유저 관리(ex. 관리자, 스태프)



## 2020.06.11

### 자유롭게 컨셉
1. 팔로우 : 영화 감독, 배우
    - 마이페이지 - 팔로우 한 감독 & 팔로우한 배우
        - 감독의 작품들 나열
        - 배우 출연작 나열
    - 추천 알고리즘
        - (평점) & 장르 + 팔로우 한 감독, 배우 출연작품 추천
        -> 평점순 5 - 10 (추천작품 개수는 추후 결정)

2. 국밥 - 든든
    - 영화 >> 몇 국밥? (ex. 이영화 보다 1국밥 할듯;;)


- 유저 : 생년월일로 나이 계산
    - 평점 표기시 성별, 나이별 표기

### 영화 데이터 입력
- ~~영화진흥원 api : 영화배우 검색 > 출연작품 리스트~~
- TMDB : 영화 리스트 + 출연 배우들

- TMDB 영화 출연 배우 + ~~영화 진흥원 api 검색~~ > 출연작품 리스트
- TMDB 영화 + 출연 배우 >> 배우로 출연 작품 검색 가능



## 2020.06.12

### DB ERD
- https://www.erdcloud.com/d/SuBgZhGQTGifi3XsH

![ERD cloud](/my_img/ERD.jpg)





## 2020.06.13

- [x] ERD cloud 모델 업데이트 - Add user favors
- [x] Update logic - loads movie data

### To do list (last update - 2020.06.13)
1) Django_api
- [x] 영화 데이터 입력 (TMDB API 이용)
- [x] django 모델 구축
- [x] serializers.py 등 DRF 환경 설정

- ~~[ ] ManyToMany field에 해당하는 중간 테이블 생성 - model (actor 수가 너무 많음)~~
    - ~~6/13 - 14 : 주말 동안 해결하기~~ 
    - ~~actor 그룹 고민해보기~~

- [x] 추천알고리즘 : 로직 고민 (주말과제)

2) Vue_front - 주말과제
- [ ] Data 받아오기
- [ ] 화면구성
    1) Home(index)
        - a) navbar
            - navigation
            - b) body
            - all movies(carousel, sort by desc)
            - user favor movie(with carousel)
            - c) pagination 
    2) User - signup, signin, signout
    3) User Favors
            - a) favor_actors
            - b) favor_direcotors
            - c) favor_genres



## 2020.06.15

### Django
- [x] 영화 추천 로직
- [x] url path
- [ ] 시간 된다면 JWT 설정

### Vue.js
- [ ] view, component 구성

### 화면 구성
- Navbar : 전체 영화 리스트, 게시판,
    - Movieda
    - 홈
    - 전체영화
    - 추천영화 ~~(좋아하는배우, 좋아하는감독, 좋아하는장르)~~

    - 영화검색
    
    - 회원가입 (~~님 환영합니다.)
    - 로그인 (로그아웃)
    
    - 마이페이지
        - 팔로우 목록 (배우, 감독)
    
    - 게시판


- Main : 추천 영화, 최신 영화(다른 영화 목록) - index
    - 추천 영화 (8개, 좋아하는 영화 장르 위주 ex. 이런 영화 어때요? 오늘 뭐 보지?)
    - 최신 영화

- MyPage : (개인정보수정), 내가 쓴 리뷰, 팔로우하는 감독, 배우, 영화 리스트 - Accounts/mypage
    - main : 간략한 내 정보, 내가 쓴 리뷰, 팔로우 배우-감독-영화 (개수)
    - 출연 영화(오늘 날짜 1-2달 작품들 리스트) or 전체 작품 리스트를 시간순

    - 더보기 (Modal 이용)
        - 리뷰
        - 배우 - 목록을 보여주고 좋아요취소기능
        - 감독
        - 영화

- 게시판 : 자유 게시판 (말머리X 단순 글 작성과 댓글) - Community/index (/community/\<int:article_pk>/)

- 영화 - Movies/index
    - 디테일 : 썸네일, 줄거리, 출연진, 감독
        - 출연진 정보 : 대표 5명 > 더보기 (전체 출연진 리스트 - Modal 이용) 이름 누르면 좋아요 기능
        





## Response Data Set 

### 1. MovieApp
#### 1-1. 영화 및 추천영화
>### /movies/
> 개수 전체
>- 'data' : 영화 전체 데이터('id', 'title', 'summary', 'release_date', 'running_time', 'poster', 'genres', 'actors', 'directors',)
>- 'recommend_movies' : 좋아요 누른 영화들의 장르 기반 추천 영화 데이터



#### 1-2. 좋아하는 배우/제작진/영화
>### /movies/like_actor/\<int:actor_pk>/
>- 로그인된 유저가 해당 배우를 좋아요 했다면 취소, 안했으면 좋아요
>- add, remove 메시지 리턴
>### /movies/like_director/\<int:director_pk>/
>- 로그인된 유저가 해당 감독을 좋아요 했다면 취소, 안했으면 좋아요
>- add, remove 메시지 리턴
>### /movies/like_movie/\<int:movie_pk>/
>- 로그인된 유저가 해당 영화를 좋아요 했다면 취소, 안했으면 좋아요
>- add, remove 메시지 리턴



#### 1-3. 영화검색

>### /movies/search/
>POST `keyword` 데이터 - form 이용?
>
>- 해당 키워드를 포함하는 영화 데이터(키워드 검색 : 영화 제목, 배우, 감독)



#### 1-4. 유저프로필

>### /profile/\<str:username>/
>- 'serializer.data': 유저 데이터('id', 'username', 'favorite_actors', >'favorite_directors', 'favorite_movies')
>- 내가 쓴 리뷰 데이터 : 유저 정보가 아닌 유저 id(pk) 값

---

### 2. 좋아요 기능 (미구현)
- django 구현 or vue 구현
- 장고 > 기존 좋아요 눌렀는지 유무  
~~- 뷰 > 어느 배우, 감독을 눌렀는지~~

#### 2-1. 커뮤니티 (홈)

>### /community/
>- 모든 게시글 보기
>- 전체 article 데이터



#### 2-2. 커뮤니티글 작성

>### /community/create/
> POST method. form data - title, content
>- 새로운 게시글 등록
>- 로그인 필수



#### 2-3. 게시글 디테일

>### /community/\<int:article_pk>/
>- `GET` method : 게시글 자세히 보기 (+ 등록된 댓글)
>- `PUT` method : 게시글 수정 (현재 로그인된 유저 == 게시글 등록 유저)
>- `DELETE` method : 게시글 삭제 (현재 로그인된 유저 == 게시글 등록 유저)



#### 2-4. 게시글 코멘트작성

>### /community/\<int:article_pk>/create_comment/
> POST method. form data - content
>- 해당 게시글에 댓글 등록
>- 로그인 필수



#### 2-5. 게시글 코멘트 수정/삭제

>### /community/\<int:article_pk>/comment/\<int:comment_pk>/
>- `PUT` method : 댓글 수정 (현재 로그인된 유저 == 댓글 등록 유저)
>
>- `DELETE` method : 댓글 삭제 (현재 로그인된 유저 == 댓글 등록 유저)

---



## 2020.06.16

필수적인 기능을 우선적으로 구현

Community, 

### Django
- [x] 영화 제작자/배우 데이터 가져오기

  -  기존: TMDB - movies/\<int:movieID\>/credits => papago api번역 

    - 데이터 파싱에서 효율성 저하​​
    - papago api 일일 사용량 초과 (limit - 약 40개 영화)

  - 개선: TMDB - movies => original_title로 naver/search_movie 사용 

    (검색되지 않는 외화 정보만 papago api로 번역 후 사용.)

    - naver 영화검색 - original_title로 검색 시 얻어지는 감독/배우 정보 사용 :movie_camera:
    - papago api 수용량 상승 :arrow_upper_right: (limit - 약 300개 영화)

  <img src="/my_img/api_capa.jpg" width="600px" height="300px" title="api_capa"></img>

- [x] models & serializer 일부 수정
  - movie - release_date | DateTimeField => DateField
  - serializer - review_detail |
- [x] views.py - scrap(영화 불러오기) fix
  - api_scrap 중 consistency가 일치하지 않는 데이터 제외
- [ ]

### Vue
- [x]
- [ ]
- [ ]
