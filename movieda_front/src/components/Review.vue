<template>
  <div class="test">
		<ReviewInput @create-review="onCreateReviewValue" :reviewData="reviewValue"/>
		<ReviewList @on-delete-review="deleteReview"/>
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
			'errorMessage': null,
		}
	},
	methods: {
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
					console.log(reviewData)
					console.log(res)
					console.log('잘 왔어요')
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
			console.log(deleteReview_URL)
			axios.post(deleteReview_URL, review_pk, config)
		}
	}
}
</script>

<style scoped>
.test {
	background-color:yellow;
	height: 10rem;
}
</style>