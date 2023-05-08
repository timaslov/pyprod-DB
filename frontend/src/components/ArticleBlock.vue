<template>
  <div class="h-full rounded-lg">
    <h1 class="text-xl text-center">
      {{ this.articleData.title }}
    </h1>

    <div v-html="this.articleData.content"></div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "article-block",

  props: {node: Object},

  data() {
    return {
      urlData: 'http://127.0.0.1:8000/api/web/v1/articles/',
      articleData: Object,
      errors: [],
    }
  },

  watch: {
    async node() {
      await this.fetchContent()
    }
  },

  async mounted() {
    await this.fetchContent()
  },

  methods: {
    async fetchContent() {
      axios
          .get(this.urlData + this.node.slug)
          .then(response => (this.articleData = response.data))
    }
  },

}
</script>
