<template>
  <div class="container">
    <h4 class="mt-3 text-left">검색어 : {{ searchData.keyword }}</h4>
    <hr>
    <div class="row" >
      <div class="col-12 col-md-6 col-lg-3 my-3" v-for="movie in searchMovies" :key="`movie_${movie.id}`">
        <div class="card jhyuk-img shadow" style="width: 16rem;">
          <img @click="onMovieSelect(movie)" :movie="movie" :src="movie.poster" class="card-img-top" alt="movie.title">
          <div class="card-body">
            <h4 class="card-title">{{ movie.title }}</h4>
            <h6 class="card-text text-secondary">{{ movie.release_date }}</h6>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SERVER_URL from '@/env.js'

export default {
  name: 'searchMovies',
  data() {
    return {
      searchMovies: [],
      searchData: {
        keyword: null,
      }
    }
  },
  methods: {
    searchMovie() {
      const searchURL = SERVER_URL + '/api/v1/movies/search/'
      axios.post(searchURL, this.searchData)
      .then(res => {
        this.searchMovies = res.data
      })
    },
    onMovieSelect(movie) {
      this.$router.push(`/movie/${movie.id}`)
    },
  },
  mounted() {
    this.searchData.keyword = this.$route.params.keyword
    this.searchMovie()
  }

}
</script>

<style>

</style>