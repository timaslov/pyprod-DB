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


    <article-to-edit-l-i
        v-for="(article, index) in this.articles"
        :key="index"
        :article="article"
    >
    </article-to-edit-l-i>
  </div>
</template>

<script>
import ArticleToEditLI from "@/components/UserCases/ArticleToEditLI.vue";
import axios from "axios";
export default {
  name: "MyArticlesView",
  components: {ArticleToEditLI},
  data() {
    return {
      // articles:
      //     [
      //       {title: "Article 1", id: "1", slug: "frontend"},
      //       {title: "Article 2", id: "2", slug: "backend"},
      //       {title: "Article 3", id: "3", slug: "vue"},
      //       {title: "Article 4", id: "4", slug: "vue_router"},
      //       {title: "Article 5", id: "5", slug: "python"},
      //     ],
      articles: [],
    }
  },

  async created() {
    await axios
        .get("http://127.0.0.1:8000/api/web/v1/articles/?author=" + "1")
        .then(response => this.articles.push(...(response.data)))

    console.log(this.article)
  },
}
</script>
