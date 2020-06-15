<template>
  <div class="home">
    <MovieList @onMovieSelected="onMovieSelected"/>
  </div>
</template>

<script>
import MovieList from '../../components/MovieList.vue'

export default {
  name: 'Home',
  components: {
    MovieList
  },
  methods: {
    onMovieSelected(movie) {
      this.$emit("onMovieSelected", movie)
    }
  }
}
</script>
