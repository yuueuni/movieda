<template>
  <div>
		
		<h3>ReviewList</h3>{{ avg_rank }}
		<ul>
			<li v-for="review in review_list" :key="review.id"> 
				{{review.rank}} | {{ review.content }} | {{ review.id }} |
				<button v-if="review.reviewer.username==cur_user" @click="deleteReview(review.id)" type="submit">삭제</button> 
			</li>
		</ul>
	</div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = "http://localhost:8000"

export default {
	name: 'ReviewList',
	data() {
		return {
			cur_user : this.$cookies.get('username'),
			review_list: [],
			avg_rank : 0,
		}
	},
	methods: {
		getReviews() {
			const review_URL = SERVER_URL + '/movies/' + this.$route.params.movieid + '/get_review/'
			axios.get(review_URL)
        .then(res => {
					this.review_list = res.data.data
					this.avg_rank = res.data.avg_rank
        })
		},
		deleteReview(review_pk) {
			this.$emit('on-delete-review', review_pk)

		},
	},
	created() {
		this.getReviews()
	},
}
</script>

<style>

</style>