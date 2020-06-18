<template>
  <div id="app">
    <div id="nav" class="sticky-top shadow-sm">
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <router-link to="/"><img src="./assets/moviedaLogo.png" width="120rem" alt="" class="d-block mx-2"></router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link">
                <router-link v-if="!isLoggedIn" :to="{ name: 'Login' }">Login</router-link>
                <span v-if="isLoggedIn"> {{username}} 님 환영합니다!</span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link">
                <router-link v-if="isLoggedIn" to="/accounts/logout" @click.native="logout">Logout</router-link>
                <router-link v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup</router-link>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link"><router-link to="/community">Community</router-link></a>
            </li>
          </ul>
          <div class="form-inline my-2 my-lg-0">
            <input v-model="keyword" id="keyword" @keypress.enter="searchKeyword(keyword)" class="form-control mr-sm-2" type="search" placeholder="Search">
            <button @click="searchKeyword(keyword)" class="btn btn-outline-secondary my-2 my-sm-0" type="submit">Search</button>
          </div>
        </div>
      </nav>
    </div>
    <router-view @submit-login-data="login" @submit-signup-data="signup" />
    
    <footer class="footer font-small fixed-bottom" style="background:aliceblue">
      <div class="footer-copyright text-center py-3">
        <span>© 2020 Copyright </span>
        <a href="https://github.com/yuueuni/movieda">MOVIEDA</a>
      </div>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'App',
  data() {
    return {
      username: this.$cookies.get('username'),
      isLoggedIn: false,
      selectedMovie: null,
      keyword: null,
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
      axios.post('/api/rest-auth/registration/', signupData)
        .then(res => {
          this.setCookie(res.data.key, signupData)
          this.$router.push({ name: 'Home' })
          alert("환영합니다 " + signupData.username + "님!")
        })
        .catch(() => alert("이미 있는 아이디입니다."))
    },

    login(loginData) {
      const loginURL = `/api/rest-auth/login/`
      console.log(loginURL)
      axios.post(loginURL, loginData)
        .then(res => {
          this.setCookie(res.data.key, loginData)
          this.isLoggedIn = true
          this.username = loginData.username
          this.$router.push({ name: 'Home' })
        })
        .catch(() => {
          alert("입력 정보가 맞지 않습니다.")
        })
    },

    logout() {
      axios.get('/api/rest-auth/logout/')
        .then(() => {
          this.$cookies.remove('auth-token')
          this.$cookies.remove('username')
          this.isLoggedIn = false
          this.$router.push({ name: 'Home' })
        })
        .catch(err => console.log(err.response))
    },
    searchKeyword(keyword) {
      this.$router.push(`/search/${keyword}`)
    }
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

#nav a {
  text-decoration: none;
  color: #797c8b;
  font-weight: bold;
}

#nav a.router-link-exact-active {
  color: #2c3e50;
}

.footer {
  font-size: small;
}

.footer a {
  color: rgb(63, 63, 63)
}
</style>
