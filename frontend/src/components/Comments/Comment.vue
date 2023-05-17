<template>
  <div
      v-if="commentIndex <= commentsQty"
      class="
      rounded-lg
      border-2
      border-gray-300
      m-5
      bg-gray-100
    "
  >
    <ul
        class="
        flex
        flex-row
        justify-between
        m-4
      "
    >
      <li
          class="
          text-lg
        "
      >
        ID пользователя: {{this.comment.author}}
      </li>

      <li>
        {{this.comment.created_on.slice(0,10) + "   " + this.comment.created_on.slice(11,16)}}
      </li>
    </ul>
    <div
        class="
        m-4
      "
    >
      {{this.comment.text}}
    </div>
  </div>
</template>

<script>
export default {
  name: "Comment",

  props: {
    comment: Object,
    commentsQty: Number,
    commentIndex: Number,
  },

}
</script>
