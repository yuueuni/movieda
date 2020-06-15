<template>
  <div class="container jutify-content-center" v-if="movie">
		<div class="card" style="width: 50rem;">
			<div class="row no-gutters">
				<div class="col-md-8">
					<img :src="movie.poster" class="card-img" :alt="movie.title">
				</div>
			<div class="col-md-4">
			<div class="card-body">
				<h5 class="card-title">{{ movie.title }}</h5>
				<p class="card-text">{{ movie.summary }}</p>
				<p class="card-text"><small class="text-muted">감독</small></p>
				<p class="text-muted" v-for="director in movie.directors" :key="director.id">{{ director.director }}</p>
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