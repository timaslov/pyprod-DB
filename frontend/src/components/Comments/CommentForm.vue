<script setup>
import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';

import { useAuthStore } from '@/stores/auth.store';
import axios from "axios";
const authStore = useAuthStore();

const schema = Yup.object().shape({
  commentText: Yup.string().required('commentText is required')
});


</script>

<template>
  <Form
      class="p-5"
      @submit="onSubmit"
      :validation-schema="schema"
      v-slot="{errors}"
      v-if="authStore.user !== null"
  >
    <Field v-slot="{ field }" name="commentText" class="">
      <textarea v-bind="field" maxlength="300" class="border-2 border-gray-400 h-24 w-full"/>
    </Field>

    <div class="flex justify-end">
      <div v-if="errors.commentText" class="mr-5">{{ 'Введите текст комментария' }}</div>
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
        "
      >
        Отправить
      </button>
    </div>
  </Form>

  <div
      v-if="authStore.user === null"
      class="p-5 text-lg"
  >
    {{ 'Авторизуйтесь, чтобы оставить комментарий' }}
  </div>

</template>

<script>
import axios from "axios";
import { useAuthStore } from '@/stores/auth.store';
export default {
  name: "CommentForm",

  props: {
    article: Object,
  },

  methods: {
    async onSubmit(values, {setErrors}) {
      const authStore = useAuthStore();

      let response
      let token = authStore.user.access
      let body = {text: values.commentText, article: this.article.id};
      let config = {headers: {Authorization: `Bearer ${token}`}};

      console.log(token);
      console.log(body);

      try {
        response = await axios.post(
            "http://localhost:8001/api/web/v1/comments/", body, config)
      } catch (error) {
        switch (error.response.status) {
          case 401:
            throw 'Ошибка 401'
          default:
            throw error.response.status
        }
      }
    }
  }
}
</script>

<style scoped>

</style>