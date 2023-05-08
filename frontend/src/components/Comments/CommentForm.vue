<script setup>
import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';

import { useAuthStore } from '@/stores/auth.store';
const authStore = useAuthStore();

const schema = Yup.object().shape({
  commentText: Yup.string().required('commentText is required')
});

function onSubmit(values, { setErrors }) {
  console.log(values);

}
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
export default {
  name: "CommentForm"
}
</script>

<style scoped>

</style>