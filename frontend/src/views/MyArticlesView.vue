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
import {useAuthStore} from "../stores/auth.store";
export default {
  name: "MyArticlesView",
  components: {ArticleToEditLI},
  data() {
    return {
      articles: [],
    }
  },

  async created() {
    const authStore = useAuthStore();
    //console.log(authStore.userInfo)

    await axios
        .get("http://127.0.0.1:8000/api/web/v1/articles/?author=" + authStore.userInfo.id)
        .then(response => this.articles.push(...(response.data)))

    //console.log(this.article)
  },
}
</script>
