<template>
	<div>
		<h1>MovieList</h1>
		<div class="container">
      <button v-if="!isHidden" @click="recommendMovies">오늘 뭐 보지?</button>
      <div class="row">
  
        <div class="col-12 col-md-6 col-lg-3 my-3" v-for="rmovie in recommendMovie" :key="`rmovie_${rmovie.id}`">
          <div class="card" style="width: 14rem;">
            <img @click="onMovieSelect(rmovie)" :rmovie="rmovie" :src="rmovie.poster" class="card-img-top" alt="rmovie.title">
            <div class="card-body">
              <h5 class="card-title">{{ rmovie.title }}</h5>
            </div>
          </div>
        </div>
      </div>
      <hr>

			<div class="row">
				<div class="col-12 col-md-6 col-lg-3 my-3" v-for="movie in movieList" :key="`movie_${movie.id}`">
					<div class="card" style="width: 16rem;">
						<img @click="onMovieSelect(movie)" :movie="movie" :src="movie.poster" class="card-img-top" alt="movie.title">
						<div class="card-body">
							<h5 class="card-title">{{ movie.title }}</h5>
							<!-- <h5 class="card-text">{{ movie.release_date }}</h5> -->
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import axios from 'axios'

	const SERVER_URL = "http://localhost:8000"

	export default {
		name: 'MovieList',
		
		data() {
			return {
        movieList: [],
        recommendMovie: [],
        isHidden: false
			};
		},
		
		methods: {
			fetchMovies() {
				axios.get(SERVER_URL + '/movies/')
					.then(res => {
						this.movieList = res.data.data
					})
			},
			onMovieSelect(movie) {
				this.$emit('onMovieSelected', movie)
      },
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
          axios.get(SERVER_URL + '/movies/', config)
            .then(res => {
              this.recommendMovie = res.data.recommend_movies
            })
            this.isHidden = true
        }
      }
		},
		created() {
			this.fetchMovies()
		}

	}

</script>

<style>
</style>