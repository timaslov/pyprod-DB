<template>
    <div>
      <h1 class="text-center pt-10 text-4xl">
        Добро пожаловать на сайт PyProd
      </h1>

      <div class="pt-10 flex items-center justify-center">
        <p class="text-center text-xl flex-initial">
          Pyprod - это бла бла... Pyprod - это бла бла...
          <br>Pyprod - это бла бла... Pyprod - это бла бла...
          <br>Pyprod - это бла бла... Pyprod - это бла бла...
          <br>Pyprod - это бла бла... Pyprod - это бла бла...
          <br>Pyprod - это бла бла... Pyprod - это бла бла...
          <br>Pyprod - это бла бла... Pyprod - это бла бла...
          <br>Pyprod - это бла бла... Pyprod - это бла бла...
          <br>Pyprod - это бла бла... Pyprod - это бла бла...
          <br>Pyprod - это бла бла... Pyprod - это бла бла...
          <br>Pyprod - это бла бла... Pyprod - это бла бла...
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
