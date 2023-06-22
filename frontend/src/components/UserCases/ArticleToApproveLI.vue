<template>
  <div class="
        rounded-lg
        border-2
        border-gray-300
        m-5
        bg-gray-100
      ">
    <div
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
        <li>
            <button
                @click="this.toggleShowButton"
                v-if="!this.articleOpened"
                class="
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
            >Показать</button>
          <button
              @click="this.toggleShowButton"
              v-if="this.articleOpened"
              class="
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
          >Скрыть</button>
        </li>
      </ul>
    </div>
    <div
        v-if="this.articleOpened"
        class="h-full rounded-lg container mx-10">

      <h1 class="text-xl text-center">
        Заголовок: {{ this.article.title }}
      </h1>

      <h1 class="text-xl text-center">
        Теги: {{ this.article.tagline }}
      </h1>

      <h1 class="text-xl text-center">
        Родитель: {{ this.article.parent_id }}
      </h1>

      <h1 class="text-xl text-center">
        Слаг: {{ this.article.slug }}
      </h1>

      <div class="w-4/5" v-html="this.article.content" ></div>

      <button
          @click="onApprove"
          class="
                  text-white
                  bg-green-600
                  hover:bg-green-800
                  duration-300
                  font-medium
                  rounded-lg
                  text-sm
                  px-5
                  py-2.5
                  my-2
                  mx-2
                "
      >
        Подтвердить
      </button>

      <button
          @click="onReject"
          class="
                  text-white
                  bg-red-600
                  hover:bg-red-800
                  duration-300
                  font-medium
                  rounded-lg
                  text-sm
                  px-5
                  py-2.5
                "
      >
        Отклонить
      </button>
    </div>
  </div>
</template>

<script>
import {useAuthStore} from "../../stores/auth.store";
import axios from "axios";

export default {
  name: "ArticleToApproveLI",
  props: {
    article: Object,
  },

  data() {
    return {
      articleOpened: false
    }
  },

  methods: {
    toggleShowButton() {
      this.articleOpened = !this.articleOpened
    },

    async onApprove() {
      const authStore = useAuthStore();
      let response
      let token = authStore.user.access
      let body = {status: "published"};
      let config = {headers: { Authorization: `Bearer ${token}` }};

      try {
        response = await axios.patch(
            "http://localhost:8001/api/web/v1/articles/" + this.article.slug + "/", body, config)
      } catch(error)
      {
        switch (error.response.status){
          case 401:
            throw 'Ошибка 401'
          default:
            throw error.response.status
        }
      }
      console.log(response)
      location.reload()
    },

    async onReject() {
      const authStore = useAuthStore();
      let response
      let token = authStore.user.access
      let body = {status: "deleted"};
      let config = {headers: { Authorization: `Bearer ${token}` }};

      try {
        response = await axios.patch(
            "http://localhost:8001/api/web/v1/articles/" + this.article.slug + "/", body, config)
      } catch(error)
      {
        switch (error.response.status){
          case 401:
            throw 'Ошибка 401'
          default:
            throw error.response.status
        }
      }
      console.log(response)
      location.reload()
    }
  },
}
</script>

<style scoped>

</style>