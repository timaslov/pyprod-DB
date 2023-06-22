<script setup>
import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';

const schema = Yup.object().shape({
  title: Yup.string().required('Title is required'),
  slug: Yup.string().required('Slug is required'),
});

</script>

<template>
  <div class="flex flex-col p-10 place-items-center">
    <Form
        @submit="onSubmit"
        v-slot="{errors}"
        :validation-schema="schema"
        class="
        flex
        flex-col
        space-y-10
        place-items-center
        p-10 border-2
        border-black
        w-[800px]
      "
    >
      <h1 class="text-center text-2xl">Создание / редактирование статьи</h1>

      <div class="grid grid-cols-3 place-items-center">
        <label>Заголовок *</label>
        <Field v-model="this.articleData.title" name="title" class="border-2" />
        <div v-if="errors.title" class="text-red-500">{{ 'Введите заголовок' }}</div>
      </div>

      <div class="grid grid-cols-3 place-items-center">
        <label>Краткое описание</label>
        <Field v-model="this.articleData.tagline" name="tagline" class="border-2" />
      </div>

      <div class="grid grid-cols-3 place-items-center">
        <label>Теги</label>
        <select class="border-2 w-[185px]" id="tagSelect">
          <option v-for="tag in this.tags" :key="tag.id" :value="tag.id">
            {{ tag.name }}
          </option>
        </select>
        <button
            @click="addTag"
            type="button"
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
          my-5
        "
        >
          Добавить
        </button>
        <a v-for="tag in this.articleData.tags" :key="tag.id" class="text-green-600"> {{tag.name}} </a>
      </div>

      <div class="grid grid-cols-3 place-items-center">
        <label>Родительская статья</label>
        <Field v-model="this.articleData.parent" v-slot="{value}" name="parent" as="select" class="border-2 w-[185px]">
          <option value="" selected>Без родителя</option>
          <option v-for="article in this.articles" :key="article.id" :value="article.id">
            {{ article.title }}
          </option>
        </Field>
      </div>

      <div class="grid grid-cols-3 place-items-center">
        <label>Картинка</label>
        <select class="border-2 w-[185px]" id="imageSelect">
          <option v-for="image in this.images" :key="image.url" :value="image.id">
            {{ image.name }}
          </option>
        </select>
        <button
            @click="addImage"
            type="button"
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
          my-5
        "
        >
          Добавить
        </button>
        <a v-for="image in this.articleData.images" :key="image.id" class="text-green-600"> {{image.name}} </a>
      </div>


      <div class="grid grid-cols-3 place-items-center">
        <label>Слаг *</label>
        <Field v-model="this.articleData.slug" name="slug" class="border-2" />
        <div v-if="errors.slug" class="text-red-500">{{ 'Введите слаг' }}</div>
      </div>

      <Field class="" name="content" v-model="this.articleData.content">
        <editor
            class=""
            api-key="no-api-key"
            id="id1"
            v-model="this.articleData.content"
            :init="{format:'html', width:'790', height:'400'}"
        />
      </Field>


      <div v-html="this.articleData.content"></div>
      <!--
      <button @click="postArticle">В консоль</button>
      -->

      <button
        type="submit"
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
          my-5
        "
      >
        Отправить
      </button>
      <label v-if="successPost || successPut" class="text-lg text-green-600">Статья успешно отправлена</label>
    </Form>
  </div>
</template>

<script>
import Editor from '@tinymce/tinymce-vue'
import axios from "axios";
import { useAuthStore } from '@/stores/auth.store';
import router from "../router";
export default {
  name: "ArticleInfoEditor",
  components: {'editor': Editor},
  data() {
    return {
      urlArticles: 'http://127.0.0.1:8000/api/web/v1/articles/',
      articles: [],
      articleData: {tags: [], images: []},
      isNewArticle: true,
      images: [],
      tags: [],
      successPost: false,
      successPut: false,
    }
  },

  async created() {
    let response1 = await axios
        .get(this.urlArticles)
        .then(response => this.articles.push(...(response.data)))

    let response2
     if (this.$route.params.slug !== undefined)
       if (this.$route.params.slug.length > 0) {
         response2 = await this.fetchArticleBySlug(this.$route.params.slug)
         this.isNewArticle = false
       }

    if (response1 && response2){
      for (let i = 0; i < this.articles.length; i++) {
        if (this.articles[i].slug === this.articleData.slug)
            this.articles.splice(i, 1);
      }
      //console.log(this.articleData.tags)
      //for (let i = 0; i < this.articleData.tags.length; i++){
      //  console.log(this.articleData.tags[i])
      //}
    }

    let response3 = await axios
        .get('http://127.0.0.1:8000/api/web/v1/images/')
        .then(response => this.images.push(...(response.data)))
    console.log(this.images)

    let response4 = await axios
        .get('http://127.0.0.1:8000/api/web/v1/tags/')
        .then(response => this.tags.push(...(response.data)))
    console.log(this.tags)
    if (response4){
      if (this.articleData.tags !== undefined) {
        for (let i = 0; i < this.articleData.tags.length; i++) {
          for (let j = 0; j < this.tags.length; j++) {
            if (this.articleData.tags[i].id === this.tags[j].id) {
              this.articleData.tags[i] = this.tags[j]
            }
          }
        }
      }
    }

  },

  methods: {
    async fetchArticleBySlug(slug) {
      //console.log(slug)
      return await axios
          .get('http://127.0.0.1:8000/api/web/v1/articles/' + slug)
          .then(response => (this.articleData = response.data))
      //console.log(this.articleData)
    },

    async onSubmit(values) {
      const authStore = useAuthStore();
      if (this.isNewArticle === true){
        if(values.parent === undefined || values.parent === "" || values.parent === null)
          values.parent = ""
        console.log(values);

        let tags_ids = []
        for(let i = 0; i < this.articleData.tags.length; i++){
          tags_ids.push(this.articleData.tags[i].id)
        }
        console.log(tags_ids)

        let images_ids = []
        for(let i = 0; i < this.articleData.images.length; i++){
          images_ids.push(this.articleData.images[i].id)
        }
        console.log(images_ids)

        let response
        let token = authStore.user.access
        let body = {title: values.title, tagline: values.tagline, content: values.content, slug: values.slug, tag_ids: tags_ids, image_ids: images_ids , parent: values.parent};
        let config = {headers: { Authorization: `Bearer ${token}` }};

        try {
          response = await axios.post(
              "http://localhost:8001/api/web/v1/articles/", body, config)
        } catch(error)
        {
          switch (error.response.status){
            case 401:
              throw 'Ошибка 401'
            default:
              throw error.response.status
          }
        }
        this.successPost = true
        setTimeout(() => {
          this.successPost = false
          router.push('/articles')
        }, "1000");
      }
      else {
        console.log('Update article');
        if(values.parent === undefined || values.parent === "" || values.parent === null)
          values.parent = ""
        console.log(values);
        console.log(this.$route.params.slug)

        let tags_ids = []
        for(let i = 0; i < this.articleData.tags.length; i++){
          tags_ids.push(this.articleData.tags[i].id)
        }
        console.log(tags_ids)

        let images_ids = []
        for(let i = 0; i < this.articleData.images.length; i++){
          images_ids.push(this.articleData.images[i].id)
        }
        console.log(images_ids)

        let response
        let token = authStore.user.access
        let body = {title: values.title, tagline: values.tagline, content: values.content, slug: values.slug, tag_ids: tags_ids, image_ids: images_ids, parent: values.parent};
        console.log(body)
        let config = {headers: { Authorization: `Bearer ${token}` }};

        try {
          response = await axios.put(
              "http://localhost:8001/api/web/v1/articles/" + this.$route.params.slug + "/", body, config)
        } catch(error)
        {
          switch (error.response.status){
            case 401:
              throw 'Ошибка 401'
            default:
              throw error.response.status
          }
        }
        this.successPut = true
        setTimeout(() => {
          this.successPut = false
          router.push('/articles')
        }, "1000");
      }
    },

    addImage() {
      let image_id = document.getElementById("imageSelect").value;

      for (let i = 0; i < this.images.length; i++) {
        if (image_id == this.images[i].id && !this.articleData.images.includes(this.images[i])) {
          this.articleData.images.push(this.images[i])
          let url = ''
          for (let i = 0; i < this.images.length; i++){
            if (this.images[i].id == image_id)
              url = this.images[i].url
          }
          console.log(this.images)
          console.log(url)
          this.articleData.content += '<img src="' + url + '">'
        }
      }
      console.log(this.articleData)

    },

    addTag() {
      let tag_id = document.getElementById("tagSelect").value;

      for (let i = 0; i < this.tags.length; i++) {
        //console.log(tag_id)
        //console.log(this.tags[i].id)
        if (tag_id == this.tags[i].id && !this.articleData.tags.includes(this.tags[i])) {
          this.articleData.tags.push(this.tags[i])
        }
      }
      console.log(this.articleData)
    },

  },

  watch: {
    $route: function () {
      this.isNewArticle = this.$route.params.slug === undefined;
    },

  },

}
</script>

<style scoped>

</style>