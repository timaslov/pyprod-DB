<template>
  <div
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
        {{this.article.title}}
      </li>
      <li>
        <router-link to ="/articleToApprove">
          <button class="
                  text-white
                  bg-amber-600
                  hover:bg-amber-800
                  duration-300
                  font-medium
                  rounded-lg
                  text-sm
                  px-5
                  py-2.5
                  mx-2
                "
          >Открыть</button>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ArticleToApproveLI",
  props: {
    article: Object,
  },
}
</script>

<style scoped>

</style>