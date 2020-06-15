<template>
  <div>
		<input v-model="reviewData.rank" type="number" min="1" max="10" id="rank" class="w-5 bg-blue"/>
		<input v-model="reviewData.content" type="text" id="content" class="w-50 bg-blue"/>
		<button @click="createReview" type="submit">댓글 입력</button>
	</div>
</template>

<script>
export default {
	name: 'ReviewInput',
	data() {
		return {
			reviewData:{
				'rank': null,
				'content': null,

			}
		}
	},
	methods: {
		createReview(reviewData) {
			console.log('---------------------')
			console.log(reviewData)
			console.log('---------------------')
			this.$emit('create-review', this.reviewData)
		},
	}
}
</script>

<style>

</style>