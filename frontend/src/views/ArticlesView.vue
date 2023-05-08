<template>
  <div>
    <subject-block :list-name="'Темы'"/>
    <comments-block/>
  </div>

</template>

<script>
import subjectBlock from "@/components/SubjectBlock.vue";
import commentsBlock from "@/components/Comments/CommentsBlock.vue";
export default {
  name: 'articles-view',

  components: {
    subjectBlock,
    commentsBlock
  }
}
</script>
