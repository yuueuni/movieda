import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/movies/Home.vue'

import MovieDetailView from '../views/movies/MovieDetailView.vue'
import SearchMovies from '../views/movies/SearchMoviesView.vue'

import LoginView from '../views/accounts/LoginView.vue'
import SignupView from '../views/accounts/SignupView.vue'

import ArticleView from '../views/articles/ArticleView.vue'
import ArticleDetailView from '../views/articles/ArticleDetailView.vue'
import ArticleCreateView from '../views/articles/ArticleCreateView.vue'

import fetchMovie from '../views/fetchView/fetchMovieView.vue'

import NotFound from '../components/404.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/search/:keyword',
    name: 'SearchMovies',
    component: SearchMovies
  },
  {
    path: '/movie/:movieid',
    name: 'MovieDetail',
    component: MovieDetailView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignupView,
  },
  {
    path: '/community',
    name: 'Community',
    component: ArticleView,
  },
  {
    path: '/community/:articleid',
    name: 'ArticleDetail',
    component: ArticleDetailView,
  },
  {
    path: '/create',
    name: 'ArticleCreateView',
    component: ArticleCreateView,
  },
  {
    path: '/fetch/:page/:pageCount',
    name: 'fetchMovie',
    component: fetchMovie,
  },
  {
    path: '*',
    name: '404Page',
    component: NotFound,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
