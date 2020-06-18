<template>
  <div class="container">
    <h1 class="mt-3">Recommendation Movies</h1>
    <div class="mx-3">
      <div v-if="isHidden" class="row border mx-auto bg-dark rounded p-3" >
        <div class="my-1 mx-auto" v-for="rmovie in recommendMovie" :key="`re_${rmovie.id}`">
          <div class="card jhyuk-img text-white bg-dark border-dark" style="width: 12rem;">
            <img @click="onMovieSelect(rmovie)" :rmovie="rmovie" :src="rmovie.poster" class="card-img-top" alt="rmovie.title" height="300rem">
            <div class="m-2">
              <h5 class="card-title">{{ rmovie.title }}</h5>
            </div>
          </div>
        </div>
      </div>
    <button @click="recommendMovies" class="btn btn-secondary my-3">오늘 뭐 보지?</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000/api/v1'

export default {
  name: 'RecommendMovies',
  data() {
    return {
      recommendMovie: [],
      isHidden: false
    };
  },
  methods: {
    recommendMovies() {
      if (!this.$cookies.get('auth-token')) {
        alert('로그인이 필요합니다!')
        this.$router.push({ name: 'Login' })
      } else {
          const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        axios.get(SERVER_URL + '/movies/recommendation/', config)
          .then(res => {
            this.recommendMovie = res.data
          })
          this.isHidden = true
      }
    }
  }
}
</script>

<style>

</style>