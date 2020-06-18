<template>
  <div class="container jutify-content-center mb-5 mt-3" v-if="movie">
		<div class="card rounded bg-light shadow p-3">
			<div class="row no-gutters">
				<div class="col-md-5">
					<img :src="movie.poster" class="card-img" :alt="movie.title">
				</div>
				<div class="col-md-7">
          <div class="text-right">
            <i v-if="isHidden" @click="likeMovie(movie.id)" class="fas fa-heart fa-2x likeHeart" style="color:crimson"></i>
            <i v-if="!isHidden" @click="likeMovie(movie.id)" class="fas fa-heart fa-2x likeHeart"></i>
          </div>
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

import SERVER_URL from '@/env.js'

export default {
	name: "movieDetailView",
	data() {
		return {
      movie: null,
      isHidden: false,
		}
	},
	components:{
		Review
	},
	methods: {
    getMovie(movieID) {
      if (this.$cookies.get('auth-token')) {
        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        axios.get('/api/v1/movies/' + movieID, config)
          .then(res => {
            this.movie = res.data.data
            if (res.data.message === 'yes') {
              this.isHidden = true
            } else if (res.data.message === 'no') {
              this.isHidden = false
            }
          })
          .catch(err => console.error(err))
      } else {
        axios.get('/api/v1/movies/' + movieID)
          .then(res => {
            this.movie = res.data.data
          })
          .catch(err => console.error(err))
      }
    },
    likeMovie(movieID) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      const likeURL =  '/api/v1/movies/like_movie/' + movieID
      axios.get(likeURL, config)
        .then(res => {
          if (res.data.message === 'add') {
            this.isHidden = true
          } else if (res.data.message === 'remove') {
            this.isHidden = false
            alert('관심 영화 목록에서 제외되었습니다. 추가를 원하시면 다시 눌러주세요.')
          }
        })
    }
  },
	mounted() {
		const movieID = this.$route.params.movieid
		this.getMovie(movieID)
	}
}
</script>

<style scoped>
.likeHeart:hover {
  cursor: pointer;
}
</style>