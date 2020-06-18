<template>
	<div class="container">
    <RecommendMovies/>
    <hr>
    <h1 class="my-3">Recently Movies</h1>
    <hr>
    <div class="row" >
      <div class="col-12 col-md-6 col-lg-3 my-3" v-for="movie in movieList" :key="`movie_${movie.id}`">
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
  import RecommendMovies from './RecommendMovies.vue'

	import SERVER_URL from '@/env.js'

	export default {
		name: 'MovieList',
		components: {
      RecommendMovies,
    },
		data() {
			return {
        movieList: [],
			};
		},
		methods: {
			fetchMovies() {
        console.log(SERVER_URL)
				axios.get('/api/v1/movies/')
					.then(res => {
						this.movieList = res.data
					})
			},
			onMovieSelect(movie) {
				this.$router.push(`/movie/${movie.id}`)
      },
		},
		created() {
			this.fetchMovies()
		}
	}
</script>

<style scoped>
	.jhyuk-img {
		transition: .3s !important;
	}
	.jhyuk-img:hover {
		transform: scale(1.1) !important;
	}
</style>