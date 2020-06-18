<template>
  <div>
  </div>
</template>

<script>
import axios from 'axios'



export default {
  name: 'fetch',
  methods: {
    fetchMovie(page, pageCount) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get('/api/v1/movies/scrap/' + page + '/' + pageCount + '/', config)
        .then(res => {
          if (res.data.message === 'success') {
            this.$router.push('/')
          }
        })
    }
  },
  mounted() {
    const page = this.$route.params.page
    const pageCount = this.$route.params.pageCount
    this.fetchMovie(page, pageCount)
  }
}
</script>
