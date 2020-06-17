<template>
  <div class="mt-5">
		<ReviewInput @create-review="onCreateReviewValue" :reviewData="reviewValue"/>
		<ReviewList @on-delete-review="deleteReview" :avgRank="avgRank" :reviewList="reviewList"/>
  </div>
</template>

<script>
import ReviewList from './ReviewList'
import ReviewInput from './ReviewInput'
import axios from 'axios'

const SERVER_URL = "http://localhost:8000"

export default {
	name: 'Review',
	components: { ReviewInput, ReviewList },
	data() {
		return {
			'reviewValue': null,
			'reviewList': [],
			'avgRank': null,
			'errorMessage': null,
		}
	},
	methods: {
		getReviews() {
			const movieID = this.$route.params.movieid
			const review_URL = SERVER_URL + '/movies/' + movieID + '/get_review/'
			axios.get(review_URL)
        .then(res => {
					const { data, avg_rank } = res.data
					this.reviewList = data
					this.avgRank = avg_rank
        })
		},
		onCreateReviewValue(reviewData) {
			const config = {
				headers: {
					Authorization: `Token ${this.$cookies.get('auth-token')}`
				}
			}
			const createReview_URL = SERVER_URL + '/movies/' + this.$route.params.movieid + '/create_review/'
			this.reviewValue = reviewData
			axios.post(createReview_URL , this.reviewValue, config)
				.then(res => {
					const { data } = res;
					this.reviewList = [...this.reviewList, data];
				})
				.catch(err => {
					console.log(err.response.data)
					alert('다시 입력해주세요!')
				})
		},
		deleteReview(review_pk) {
			this.reviewList = this.reviewList.filter(review => review.id!==review_pk)
			const config = {
				headers: {
					Authorization: `Token ${this.$cookies.get('auth-token')}`
				}
			}
			const deleteReview_URL = SERVER_URL + '/movies/' + this.$route.params.movieid + '/delete_review/' + review_pk
			axios.post(deleteReview_URL, review_pk, config)
		},
	},
	mounted() {
		this.getReviews()
	}
}
</script>

<style scoped>
</style>