<template>
  <div>
    <table class="table table-hover">
      <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col">글 제목</th>
          <th scope="col">영화 제목</th>
          <th scope="col">작성자</th>
        </tr>
      </thead>
      <tbody>
        <tr @click="onArticleSelect(article)" :article="article" v-for="article in articles" :key="article.id">
          <th scope="row">{{ article.id }}</th>
          <td>{{ article.title }}</td>
          <td>{{ article.movies }}</td>
          <td>{{ article.writer.username }}</td>
        </tr>
      </tbody>
    </table>
    <p v-if="articles.length === 0" class="mt-3">아직 등록된 글이 없습니다.</p>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'ArticleList',
  data() {
    return {
      articles: Object,
    }
  },
  methods: {
    onArticleSelect(article) {
      this.$router.push(`/community/${article.id}`)
    },
    getArticle() {
      axios.get(SERVER_URL + '/community/')
        .then(res => {
          this.articles = res.data
        })
    }
  },
  created() {
    this.getArticle()
  },
  mounted() {
    this.getArticle()
  }
}
</script>

<style scoped>
tr:hover {
  cursor: pointer;
}
</style>