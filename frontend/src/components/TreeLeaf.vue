<template>
  <div v-if='node.status === "published"'>
    <div
      class="text-amber-700 text-xl cursor-pointer"
      v-if="pathArray[pathArray.length-1] === node.slug"
    >
      {{ node.title }}
    </div>
    <div
      class="text-amber-500 text-xl cursor-pointer"
      v-else
    >
      {{ node.title }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'tree-leaf',

  props: {
    node: Object,
    pathArray: Array,
  },

}
</script>
