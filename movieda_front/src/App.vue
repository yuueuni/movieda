<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link v-if="!isLoggedIn" :to="{ name: 'Login' }">Login |</router-link>
      <router-link v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup |</router-link>
      <span v-if="isLoggedIn"> {{username}} 님 환영합니다.|</span>
      <router-link v-if="isLoggedIn" to="/accounts/logout" @click.native="logout"> Logout</router-link>
    </div>
    <router-view @submit-login-data="login" @submit-signup-data="signup" @onMovieSelected="onMovieSelect"/>
    <div v-if="selectedMovie">
      {{ selectedMovie.id }}
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import MovieDetailView from './views/movies/MovieDetailView.vue'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'App',
  
  data() {
    return {
      username: null,
      isLoggedIn: false,
      errorMessage: false,
      selectedMovie: null,
    }
  },
  
  methods: {
    setCookie(token) {
      this.$cookies.set('auth-token', token)
      this.isLoggedIn = true
    },

    signup(signupData){
      axios.post(SERVER_URL + '/rest-auth/registration/', signupData)
        .then(res => {
          this.setCookie(res.data.key)
          this.$router.push({ name: 'Home' })
        })
        .catch(err => this.errorMessage = err.response.data)
    },

    login(loginData) {
      axios.post(SERVER_URL + '/rest-auth/login/', loginData)
        .then(res => {
          this.setCookie(res.data.key)
          this.isLoggedIn = true
          this.$router.push({ name: 'Home' })
          this.username = loginData.username
        })
        .catch(() => alert("회원정보가 잘못되었습니다."))
    },

    logout() {
      axios.get(SERVER_URL + '/rest-auth/logout/')
        .then(() => {
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          this.$router.push({ name: 'Home' })
        })
        .catch(err => console.log(err.response))
    },
    onMovieSelect(movie) {
      this.selectedMovie = movie
      console.log(movie)
      this.$router.push({ name: 'movieDetailView', params:""})
    },
  },

  mounted() {
    this.isLoggedIn = this.$cookies.isKey('auth-token')
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
