<template>
  <div class="h-full rounded-lg container mx-10">

    <h1 class="text-xl text-center">
      Заголовок: {{ this.article.title }}
    </h1>

    <h1 class="text-xl text-center">
      Теги: {{ this.article.tags }}
    </h1>

    <h1 class="text-xl text-center">
      Родитель: {{ this.article.parent_id }}
    </h1>

    <h1 class="text-xl text-center">
      Слаг: {{ this.article.slug }}
    </h1>

    <div v-html="this.article.content" ></div>

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
</template>

<script>
export default {
  name: "ArticleToApprove",
  props: {
    article: Object
  },
}
</script>

<style scoped>

</style>