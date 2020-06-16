<template>
  <div class="container jutify-content-center mb-5 mt-3" v-if="movie">
		<div class="card rounded bg-light shadow">
			<div class="row no-gutters">
				<div class="col-md-5">
					<img :src="movie.poster" class="card-img" :alt="movie.title">
				</div>
				<div class="col-md-7">
					<div class="card-body">
						<h1 class="card-title font-weight-bold">{{ movie.title }}</h1>
						<p class="cart-text">{{movie.release_date}}, {{movie.original_title}} {{movie.running_time}}분</p>
						
						<div class="mt-5">
							<hr>
							<h3>줄거리</h3>
							<p class="card-text px-5">{{ movie.summary }}</p>
							<hr>
						</div>
						<p class="card-text mb-3">감독</p>
						<p class="text-muted" v-for="director in movie.directors" :key="director.id">{{ director.director }}</p>
						<hr>
						<p class="card-text mb-3">배우</p>
						<div class="row">
							<div class="text-muted col-4 mb-3" v-for="actor in movie.actors" :key="actor.id">{{ actor.actor }}</div>
						</div>
						
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

<style scoped>
</style>