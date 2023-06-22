<template>
  <div
      class="
      rounded-lg
      border-2
      border-gray-300
      m-5
      bg-gray-100
    "
  >
    <ul
        class="
        flex
        flex-row
        justify-between
        m-4
      "
    >
      <li
          class="
          text-lg
        "
      >
        {{this.article.title}}
      </li>
      <li
          class="
          text-lg
        "
      >
        Статус: {{this.article.status}}
      </li>
      <li>
        <router-link :to = this.editorLink>
          <button class="
                  text-white
                  bg-amber-600
                  hover:bg-amber-800
                  duration-300
                  font-medium
                  rounded-lg
                  text-sm
                  px-5
                  py-2.5
                  mx-2
                "
          >Изменить</button>
        </router-link>
        <button
            @click="deleteArticle"
            class="
                text-white
                bg-red-600
                hover:bg-amber-800
                duration-300
                font-medium
                rounded-lg
                text-sm
                px-5
                py-2.5
              "
        >Удалить</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
import {useAuthStore} from "../../stores/auth.store";
export default {
  name: "ArticleToEditLI",

  props: {
    article: Object,
  },

  data() {
    return {
      editorLink: String
    }
  },

  mounted() {
    this.editorLink = '/editor' + '/' + this.article.slug
  },

  methods: {
    async deleteArticle() {
      console.log("delete article")

      const authStore = useAuthStore();
      let response
      let token = authStore.user.access
      let config = {headers: { Authorization: `Bearer ${token}` }};
      try {
        response = await axios.delete(
            "http://localhost:8001/api/web/v1/articles/" + this.article.slug, config)
      } catch(error)
      {
        switch (error.response.status){
          case 401:
            throw 'Ошибка 401'
          default:
            throw error.response.status
        }
      }
      location.reload()
    }
  }
}
</script>

<style scoped>

</style>
