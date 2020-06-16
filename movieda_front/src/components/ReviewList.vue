<template>
  <div>
		<h3 class="text-left">ReviewList<span class="badge badge-info mx-3">{{ avgRank }}</span></h3>
		<ul class="list-group">
			<li v-for="review in reviewList" :key="review.id" class="list-group-item text-left my-flex"> 
				<span style="font-weight: 700;" class="mr-2">{{ review.reviewer.username }} |</span>
				<span style="font-size: 20px;">{{ review.content }}</span>
				<h5><span class="badge badge-warning rounded-circle ml-3">{{ review.rank }}</span></h5>
				<div style="flex: 1;" />
				<button class="btn btn-danger p-1" style="height: 30px !important;" v-if="review.reviewer.username==cur_user" @click="deleteReview(review.id)" type="submit">삭제</button> 
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

<style scoped>
.my-flex {
	display: flex !important;
	align-items: center;
}
</style>