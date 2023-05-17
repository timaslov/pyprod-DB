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

      <button class="
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

      <button class="
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
  },
}
</script>

<style scoped>

</style>