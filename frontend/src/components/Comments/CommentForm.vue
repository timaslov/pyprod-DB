<script setup>
import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';

import { useAuthStore } from '@/stores/auth.store';
import axios from "axios";
const authStore = useAuthStore();

const schema = Yup.object().shape({
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
    <Field v-model="commText" v-slot="{ field }" id="commentField" name="commentText" class="">
      <textarea id="commentTextArea" v-bind="field" maxlength="300" class="border-2 border-gray-400 h-24 w-full"/>
    </Field>

    <div class="flex justify-end">
      <div v-if="warningNoText" class="mr-5">{{ 'Введите текст комментария' }}</div>
      <div v-if="success" class="mr-5">{{ 'Комментарий отправлен' }}</div>
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

  data() {
    return {
      commText: "",
      warningNoText: false,
      success: false,
    }
  },

  methods: {
    async onSubmit(values, {setErrors}) {
      console.log(values.commentText)
      if (values.commentText === ''){
        this.warningNoText = true
      }
      else {
        const authStore = useAuthStore()
        let response
        let token = authStore.user.access
        let body = {text: values.commentText, article: this.article.id};
        let config = {headers: {Authorization: `Bearer ${token}`}};

        //console.log(token);
        //console.log(body);

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
        this.commText = '';
        this.warningNoText = false;
        this.success = true;
        setTimeout(() => {
          this.success = false;
        }, "3000");
        //location.reload();
      }
    }
  }
}
</script>

<style scoped>

</style>