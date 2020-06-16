<template>
  <div class="container mt-3">
    <p class="text-left"><router-link to="/community">돌아가기</router-link></p>
    <div class="border rounded py-3">
      <div class="px-3">
        <h2 class="mb-2 text-left"><span class="badge badge-info">{{ article.movies }}</span></h2>
        <div class="d-flex justify-content-between align-items-end">
          <h1 class="text-left">{{ article.title }}</h1>
          <p class="mb-0 text-right">{{ article.created_at }}</p>
        </div>
      </div>
      <hr>
      <div class="text-left px-3" style="min-height:20rem">
        {{ article.content }}
      </div>
    </div>
    <div class="d-flex justify-content-center my-3">
      <button v-if="isHidden" @click="deleteArticle(article.id)" class="btn btn-secondary">삭제</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'ArticleDetail',
  data() {
    return {
      article: Object,
      isHidden: false,
    }
  },
  methods: {
    getArticle(articleID) {
      axios.get(SERVER_URL + '/community/' + articleID)
        .then(res => {
          this.article = res.data
          const currnetUSER = this.$cookies.get('username')
          if (this.article.writer.username === currnetUSER) {
            this.isHidden = true
          }
        })
        .catch(err => console.log(err))
    },
    deleteArticle(articleid) {
			const config = {
				headers: {
					Authorization: `Token ${this.$cookies.get('auth-token')}`
				}
      }
      const deleteArticleURL = SERVER_URL + '/community/' + articleid
      axios.delete(deleteArticleURL, config)
      this.$router.push(`/community/`)
    }
  },
  mounted() {
    const articleID = this.$route.params.articleid
    this.getArticle(articleID)
  }
}
</script>

<style>

</style>