<template>
  <div v-if="movie">
		<h1>MovieDetail</h1>
  </div>
</template>

<script>
export default {
	name: "movieDetail",
	props: {
		movie: Object,
	},
}
</script>

<style>

</style>