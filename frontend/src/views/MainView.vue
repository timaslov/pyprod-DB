<template>
    <div>
      <h1 class="text-center pt-10 text-4xl">
        Добро пожаловать на сайт PyProd
      </h1>

      <div class="pt-10 flex items-center justify-center">
        <p class="text-center text-xl flex-initial">
          Здесь вы можете найти полезные статьи в сфере IT.
          <br>Или можете писать их сами, если Вы наделены правами модератора.
          <br>Навигация по статьям имеет древовидную структуру, которая может
          <br>подсказать Вам, какие темы являются смежными и могут быть полезны.
          <br>Ниже представлены фундаментальные темы, которые являются
          <br>родительскими для всех остальных.
        </p>
      </div>

      <div class="p-10">
        <subject-block :list-name="'Темы'"/>
      </div>
    </div>
</template>

<script>
import subjectBlock from "@/components/SubjectBlock.vue";
export default {
  name: "main-view",

  components: {subjectBlock},
}
</script>
