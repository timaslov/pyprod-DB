<template>
  <div
      class="
      container
      mx-auto
      my-5
      border-2
      border-gray-300
      rounded-lg
    "
  >
    <h1
        class="
        text-xl
        text-center
      "
    >
      Статьи
    </h1>
    <h1
        v-if="articles.length === 0"
        class="
        text-lg
        text-center
      "
    >
      Нет статей к подтверждению
    </h1>


    <article-to-approve-l-i
        v-for="(article, index) in this.articles"
        :key="index"
        :article="article">
    </article-to-approve-l-i>
  </div>
</template>

<script>
import ArticleToApproveLI from "@/components/UserCases/ArticleToApproveLI.vue";
import axios from "axios";
export default {
  name: "ArticlesToApprove",
  components:{ArticleToApproveLI},
  data() {
    return {
      // articles:
      //     [
      //       {title: "Article 1", id: "1", slug: "frontend"},
      //       {title: "Article 2", id: "2", slug: "backend"},
      //       {title: "Article 3", id: "3", slug: "vue"},
      //     ],
      articles: [],
    }
  },

  async created() {
    await axios
        .get("http://127.0.0.1:8000/api/web/v1/articles/?status=draft")
        .then(response => this.articles.push(...(response.data)))

    console.log(this.article)
  },
}
</script>

<style scoped>

</style>