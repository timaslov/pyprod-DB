<script setup>
import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';

const schema = Yup.object().shape({
  title: Yup.string().required('Title is required'),
  slug: Yup.string().required('Slug is required'),
});
function onSubmit(values) {
  console.log(values);
}
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
      <h1 class="text-center text-2xl">Инфо о статье</h1>

      <div class="grid grid-cols-2 place-items-center">
        <label>Заголовок *</label>
        <Field name="title" class="border-2" />
        <div v-if="errors.title" class="text-red-500">{{ 'Введите заголовок' }}</div>
      </div>

      <div class="grid grid-cols-2 place-items-center">
        <label>Теги</label>
        <Field name="tagline" class="border-2" />
      </div>

      <div class="grid grid-cols-2 place-items-center">
        <label>Родитель</label>
        <Field v-slot="{ parentField }" name="tagline">
          <select v-bind="parentField" class="border-2 w-[185px]"></select>
        </Field>
      </div>

      <div class="grid grid-cols-2 place-items-center">
        <label>Слаг *</label>
        <Field name="slug" class="border-2" />
        <div v-if="errors.slug" class="text-red-500">{{ 'Введите слаг' }}</div>
      </div>

      <articleEditor></articleEditor>

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
        Запостить
      </button>
    </Form>
  </div>
</template>

<script>
import articleEditor from "@/components/ArticleEditor.vue";
export default {
  name: "ArticleInfoEditor",
  components: {articleEditor},

}
</script>

<style scoped>

</style>