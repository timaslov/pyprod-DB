<script setup>
import {useTreeStore} from "@/stores/tree.store";
const treeStore = useTreeStore();
</script>

<template>
  <div
      class="
      container
      mx-auto
      my-5
      border-2
      border-gray-300
      rounded-lg
    "
      v-show="treeStore.isTreeVisible"
  >
    <h1
        class="
        text-xl
        text-center
      "
    >
      Комментарии
    </h1>

    <comment-form :article="this.article"/>

    <comment
        v-for="(comment, index) in this.comments"
        :key="comment"
        :comment="comment"
        :commentsQty="this.commentsToShowQty"
        :commentIndex="index+1"
    >
    </comment>

    <button
        @click="showMoreComments"
        v-if="this.comments.length !== this.commentsToShowQty"
        class="
        flex
        mx-auto
      "
    >
      Загрузить еще комменты
    </button>
  </div>
</template>

<script>
import comment from "@/components/Comments/Comment.vue";
import commentForm from "@/components/Comments/CommentForm.vue";
import axios from "axios";
export default {
  components: {comment, commentForm},

  name: "CommentsBlock.vue",

  data() {
    return {
      // comments:
      //     [
      //       {userName: "User1", date: "25.05.2023 12:04", text: "Ничего не понятно, но очень интересно"},
      //       {userName: "User2", date: "15.04.2023 11:54", text: "Какой-то текст"},
      //       {userName: "User3", date: "05.03.2023 21:36", text: "Что-то о чем-то зачем-то"},
      //       {userName: "User4", date: "21.02.2022 06:32", text: "Лалалала лалалала лалалалал лалалла"},
      //       {userName: "User5", date: "07.02.2023 13:00", text: "Какой-то текст снова"},
      //       {userName: "User6", date: "11.01.2023 15:24", text: "Первый коммент (или последний?)"},
      //       {userName: "User7", date: "25.05.2023 12:04", text: "Ничего не понятно, но очень интересно"},
      //       {userName: "User8", date: "15.04.2023 11:54", text: "Какой-то текст"},
      //       {userName: "User9", date: "05.03.2023 21:36", text: "Что-то о чем-то зачем-то"},
      //       {userName: "User10", date: "21.02.2022 06:32", text: "Лалалала лалалала лалалалал лалалла"},
      //       {userName: "User11", date: "07.02.2023 13:00", text: "Какой-то текст снова"},
      //       {userName: "User12", date: "11.01.2023 15:24", text: "Первый коммент (или последний?)"},
      //     ],
      comments: [],
      commentsToShowQty: 0,
      article: {},
    }
  },



  async created() {
    await this.fetchArticle(this.$route.params.slug)
    await this.fetchComments(this.article.id)
    this.calcCommentsToShow();
  },

  methods: {
    showMoreComments() {
      if (this.comments.length > this.commentsToShowQty)
      {
        this.calcCommentsToShow();
      }
    },

    calcCommentsToShow() {
      return this.commentsToShowQty +=
          this.comments.length - this.commentsToShowQty < 5 ?
              this.comments.length - this.commentsToShowQty : 5;
    },

    async fetchArticle(slug){
      await axios
          .get("http://127.0.0.1:8000/api/web/v1/articles/" + slug)
          .then(response => this.article = response.data)

      console.log(this.article)
    },

    async fetchComments(article_id){
      await axios
          .get("http://127.0.0.1:8000/api/web/v1/comments/?article_id=" + article_id)
          .then(response => this.comments.push(...(response.data)))

      console.log(this.comments)
    }
  },

  watch: {
    $route: async function () {
      this.comments = []
      this.commentsToShowQty = 0
      await this.fetchArticle(this.$route.params.slug)
      await this.fetchComments(this.article.id)
      this.calcCommentsToShow();
      console.log(this.comments)
      console.log(this.commentsToShowQty)
    },
  },

}
</script>
