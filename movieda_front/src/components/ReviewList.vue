<template>
  <div>
		
		<h3>ReviewList</h3>{{ avgRank }}
		<ul>
			<li v-for="review in reviewList" :key="review.id"> 
				{{review.rank}} | {{ review.content }} | {{ review.id }} |
				<button v-if="review.reviewer.username==cur_user" @click="deleteReview(review.id)" type="submit">삭제</button> 
			</li>
		</ul>
	</div>
</template>

<script>
export default {
	name: 'ReviewList',
	props: {
		reviewList: Array,
		avgRank: Number,
	},
	data() {
		return {
			cur_user : this.$cookies.get('username'),
		}
	},
	methods: {
		deleteReview(review_pk) {
			this.$emit('on-delete-review', review_pk)
		},
	}
}
</script>

<style>

</style>