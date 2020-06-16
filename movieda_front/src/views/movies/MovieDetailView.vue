<template>
  <div class="container jutify-content-center" v-if="movie">
		<div class="card" style="width: 50rem;">
			<div class="row no-gutters">
				<div class="col-md-8">
					<img :src="movie.poster" class="card-img" :alt="movie.title">
				</div>
				<div class="col-md-4">
					<div class="card-body">
						<h5 class="card-title">{{ movie.title }}</h5>
						<p class="card-text">{{ movie.summary }}</p>
						<p class="card-text"><small class="text-muted">감독</small></p>
						<p class="text-muted" v-for="director in movie.directors" :key="director.id">{{ director.director }}</p>
						<br>
					</div>
				</div>
			</div>
		</div>
	<Review/>
  </div>
</template>

<script>
import Review from '../../components/Review.vue'
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
	name: "movieDetailView",
	data() {
		return {
			movie: null,
		}
	},
	components:{
		Review
	},
	methods: {
    getMovie(movieID) {
      axios.get(SERVER_URL + '/movies/' + movieID)
        .then(res => {
          this.movie = res.data
				})
				.catch(err => console.error(err))
    }
	},
	mounted() {
		const movieID = this.$route.params.movieid
		this.getMovie(movieID)
	}
}
</script>

<style>

</style>