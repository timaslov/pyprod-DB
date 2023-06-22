<template>
  <div class="flex flex-col place-items-center m-10">
    <label class="m-2 text-lg"> Введите ключевое слово, которое содержится в названии, в тегах или в теле статьи. </label>
    <label class="m-2 text-lg"> Что ищем? </label>
    <div>
      <input v-model="request" class="border-2 w-[400px]">
      <button
          @click="find"
          class="
                text-white
                bg-amber-600
                hover:bg-amber-800
                duration-300
                font-medium
                rounded-lg
                text-lg
                mx-2
                px-4
              "
      >&#x1F50D</button>
    </div>

    <div v-if="isResVisible" class="border-2 rounded-lg m-2 container flex flex-col" >
      <h1 class="mx-auto  text-lg"> Результаты поиска по названиям статей: </h1>
      <h1 v-if="resByTitle.length === 0" class="mx-auto  text-lg"> В названиях ничего не найдено. </h1>
      <div v-for="article in resByTitle" :key="article.id">
        <router-link
            :to='{path:`articles/` + article.slug}'
            class="text-blue-600 m-2 text-lg"
                    >
          {{article.title}}
        </router-link>
      </div>
    </div>

    <div v-if="isResVisible" class="border-2 rounded-lg m-2 container flex flex-col" >
      <h1 class="mx-auto  text-lg"> Результаты поиска по тегам: </h1>
      <h1 v-if="resByTags.length === 0" class="mx-auto  text-lg"> В тегах ничего не найдено. </h1>
      <div v-for="article in resByTags" :key="article.id">
        <router-link
            :to='{path:`articles/` + article.slug}'
            class="text-blue-600 m-2 text-lg"
        >
          {{article.title}}
        </router-link>
      </div>
    </div>

    <div v-if="isResVisible" class="border-2 rounded-lg m-2 container flex flex-col" >
      <h1 class="mx-auto  text-lg"> Результаты поиска по словам в статье: </h1>
      <h1 v-if="resByContent.length === 0" class="mx-auto  text-lg"> В теле статей ничего не найдено. </h1>
      <div v-for="article in resByContent" :key="article.id">
        <router-link
            :to='{path:`articles/` + article.slug}'
            class="text-blue-600 m-2 text-lg"
        >
          {{article.title}}
        </router-link>
      </div>
    </div>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SearchArticle",

  data() {
    return {
      request: "",
      articles: [],
      resByTitle: [],
      resByTags: [],
      resByContent: [],
      isResVisible: false,
    }
  },

  methods: {
    find(){
      if (this.request !== ""){
        this.isResVisible = true
        // Поиск по названию (тайтлу)
        this.resByTitle = []
        for (let i = 0; i < this.articles.length; i++){
          if (this.articles[i].title.toLowerCase().includes(this.request.toLowerCase())){
            this.resByTitle.push(this.articles[i])
          }
        }

        // Поиск по тегам
        this.resByTags = []
        for (let i = 0; i < this.articles.length; i++) {
          for (let j = 0; j < this.articles[i].tags.length; j++){
            if (this.articles[i].tags[j].name.toLowerCase().includes(this.request.toLowerCase()))
              this.resByTags.push(this.articles[i])
          }
        }

        // Поиск по словам в статье
        this.resByContent = []
        for (let i = 0; i < this.articles.length; i++) {
          if (this.articles[i].content.toLowerCase().includes(this.request.toLowerCase()))
            this.resByContent.push(this.articles[i])
        }
      }
    },

    toggleResVisibility(){
      this.isResVisible = !this.isResVisible
    }
  },

  async created() {
    await axios
        .get("http://127.0.0.1:8000/api/web/v1/articles/?status=published")
        .then(response => this.articles.push(...(response.data)))
    console.log(this.articles)
  },

}
</script>

<style scoped>

</style>