<template>
  <div class="mx-auto my-3 w-50" style="letter-spacing:.5px;">
    <h1 class="my-2">New Article</h1>
    <hr>
    <div class="d-block p-3 mx-auto">
      <div class="input-block w-100">
        <label for="title" class="sr-only">title</label>
        <input v-model="articleData.title" id="title" type="text" class="form-control" placeholder="Title" required autofocus>
      </div>
      <div class="input-block w-100">
        <label for="movies" class="sr-only">movie title</label>
        <input v-model="articleData.movies" id="movies" type="text" class="form-control" placeholder="Movie Title" required>
      </div>
      <div class="input-block w-100">
        <label for="content" class="sr-only">content</label>
        <textarea v-model="articleData.content" id="conent" type="text" class="form-control" style="min-height:10rem;" placeholder="Content" required></textarea>
      </div>
      <div class="my-3">
        <button class="btn btn-secondary" @click="createArticle">등록</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'ArticleCreate',
  data() {
    return {
      articleData: {
        title: null,
        movies: null,
        content: null,
      }
    }
  },
  methods: {
    createArticle() {
      const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
      const createArticleURL = SERVER_URL + '/community/create/'
      axios.post(createArticleURL, this.articleData, config)
      .then(res => {
        this.$router.push(`/community`)
        console.log(res.data)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  created() {
    if (!this.$cookies.isKey('auth-token')){
      alert('로그인이 필요합니다.')
      this.$router.push(`/login`)
    }
  }
}
</script>

<style>

</style>