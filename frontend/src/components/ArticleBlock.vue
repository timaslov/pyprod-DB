<template>
  <div class="h-full rounded-lg">
    <div class="grid grid-cols-3 place-items-center">
      <h1></h1>
      <h1 class="text-xl text-center">
        {{ this.articleData.title }}
      </h1>
      <h1 class="text-lg text-center">
        ID автора: {{this.articleData.author === null ? 'null' : this.articleData.author }}
      </h1>
    </div>

    <hr class="border-t-2 m-2">

    <h1 class="text-center"> {{this.articleData.tagline}} </h1>

    <hr class="border-t-2 m-2">

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
