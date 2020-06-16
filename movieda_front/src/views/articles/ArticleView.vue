<template>
  <div class="container">
    <div class="alert alert-warning" role="alert">
      현재 게시판에 작성된 글의 수정이 불가능합니다. 이용에 불편을 드려 죄송합니다.
    </div>
    <h1 class="mt-3 mb-0">Community</h1>
    <div class="text-right mb-2 notext">
      <button class="btn btn-outline-secondary ml-0"><router-link to="/create"><span class="notext">글 작성</span></router-link></button>
    </div>
    <ArticleList />
  </div>
</template>

<script>
import ArticleList from '../../components/ArticleList.vue'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  }

}
</script>

<style scoped>
.notext {
  color: #6c757d;
  text-decoration: none;
}

.notext :hover{
  color: white;
  text-decoration: none;
}
</style>