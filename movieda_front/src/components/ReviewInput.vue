<template>
  <div class="input-group mb-3">
		<select id="movieRank" name="평점" @change="onChangeRank($event)" class="pl-2">
			<option value="1">1</option><option value="2">2</option>
			<option value="3">3</option><option value="4">4</option>
			<option value="5">5</option><option value="6">6</option>
			<option value="7">7</option><option value="8">8</option>
			<option value="9">9</option><option value="10">10</option>
		</select>
		<input @keypress.enter="createReview" v-model="reviewData.content" type="text" class="w-50 form-control" placeholder="리뷰를 입력해주세요."/>
		<div class="input-group-append">
			<button @click="createReview" type="submit" class="btn btn-outline-secondary">댓글 입력</button>
		</div>
	</div>
</template>

<script>

export default {
	name: 'ReviewInput',
	data() {
		return {
			reviewData:{
				rank: 1,
				content: null,
			}
		}
	},
	methods: {
		createReview() {
			this.$emit('create-review', this.reviewData)
		},
		onChangeRank(e) {
			this.reviewData.rank = e.target.value
		}
	}
}
</script>

<style scoped>

</style>