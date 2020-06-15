<template>
  <div class="container" v-if="movie">
		<div class="card" style="max-width: 540px;">
			<div class="row no-gutters">
				<div class="col-md-8">
					<img :src="movie.poster" class="card-img" :alt="movie.title">
				</div>
			<div class="col-md-4">
			<div class="card-body">
				<h5 class="card-title">Card title</h5>
				<p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
				<p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
			</div>
		</div>
  </div>
</div>
		
  </div>
</template>

<script>
export default {
	name: "movieDetailView",
	props: {
		movie: Object,
	},
}
</script>

<style>

</style>