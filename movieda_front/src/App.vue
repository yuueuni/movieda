<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link v-if="!isLoggedIn" :to="{ name: 'Login' }">Login |</router-link>
      <router-link v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup |</router-link>
      <span v-if="isLoggedIn"> {{username}} 님 환영합니다! </span>
      <router-link v-if="isLoggedIn" to="/accounts/logout" @click.native="logout"> Logout</router-link>
    </div>
    <router-view @submit-login-data="login" @submit-signup-data="signup" @onMovieSelected="onMovieSelect" :movie="selectedMovie"/>
  </div>
</template>

<script>
import axios from 'axios'
// import Home from './views/movies/Home.vue'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'App',
  // components: {Home},
  data() {
    return {
      username: this.$cookies.get('username'),
      isLoggedIn: false,
      errorMessage: false,
      selectedMovie: null,
    }
  },
  
  methods: {
    setCookie(token, data) {
      this.$cookies.set('auth-token', token)
      this.$cookies.set('username', data.username)
      this.username = data.username
      this.isLoggedIn = true
    },

    signup(signupData){
      axios.post(SERVER_URL + '/rest-auth/registration/', signupData)
        .then(res => {
          this.setCookie(res.data.key, signupData)
          this.$router.push({ name: 'Home' })
        })
        .catch(err => this.errorMessage = err.response.data)
    },

    login(loginData) {
      axios.post(SERVER_URL + '/rest-auth/login/', loginData)
        .then(res => {
          this.setCookie(res.data.key, loginData)
          this.isLoggedIn = true
          this.username = loginData.username
          this.$router.push({ name: 'Home' })
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
      console.log(this.selectedMovie)
      this.$router.push({ name: 'MovieDetail', params: {movieid: this.selectedMovie.id}})
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
