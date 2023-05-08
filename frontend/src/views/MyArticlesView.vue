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
        v-for="(n, index) in this.articles"
        :key="index"
        :article="this.articles[index]"
    >
    </article-to-edit-l-i>
  </div>
</template>

<script>
import ArticleToEditLI from "@/components/UserCases/ArticleToEditLI.vue";
export default {
  name: "MyArticlesView",
  components: {ArticleToEditLI},
  data() {
    return {
      articles:
          [
            {title: "Article 1", id: "1", slug: "art1"},
            {title: "Article 2", id: "2", slug: "art2"},
            {title: "Article 3", id: "3", slug: "art3"},
          ],
    }
  },
}
</script>

<style scoped>

</style>