<template>
	<div>
		<h1>MovieList</h1>
		<div class="container">
			<div class="row">
				<div class="col-12 col-md-6 col-lg-3 my-3" v-for="movie in movieList" :key="`movie_${movie.id}`">
					<div class="card" style="width: 16rem;">
						<img @click="onMovieSelect(movie)" :movie="movie" :src="movie.poster" class="card-img-top" alt="movie.title">
						<div class="card-body">
							<h5 class="card-title">{{ movie.title }}</h5>
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
				movieList: []
			};
		},
		
		methods: {
			fetchMovies() {
				axios.get(SERVER_URL + '/movies/')
					.then(res => {
						console.log(res)
						this.movieList = res.data
					})
			},
			onMovieSelect(movie) {
				this.$emit('onMovieSelected', movie)
			}
		},
		created() {
			this.fetchMovies()
		}

	}

</script>

<style>
</style>