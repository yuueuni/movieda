<template>
	<div class="container">
    <h1 class="my-2">Recommendation Movies</h1>
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
      <button @click="recommendMovies" class="btn btn-secondary mt-3">오늘 뭐 보지?</button>
    </div>
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
						this.movieList = res.data
					})
			},
			onMovieSelect(movie) {
				this.$router.push(`/movie/${movie.id}`)
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
          axios.get(SERVER_URL + '/movies/recommendation/', config)
            .then(res => {
              this.recommendMovie = res.data
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

<style scoped>
	.jhyuk-img {
		transition: .3s !important;
	}
	.jhyuk-img:hover {
		transform: scale(1.1) !important;
	}
</style>