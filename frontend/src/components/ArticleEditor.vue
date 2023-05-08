<template>
    <editor
        class="w-full"
        api-key="no-api-key"
        id="id1"
        v-model="content"
    />
  <div v-html="content"></div>
  <button @click="postArticle">В консоль</button>
</template>

<script>
import Editor from '@tinymce/tinymce-vue'
export default {
  name: "ArticleEditor.vue",

  data() {
    return {
      content: '',
    }
  },

  components: {
    'editor': Editor
  },

  methods: {
    postArticle() {
      console.log(this.content)
    }
  },

}
</script>
