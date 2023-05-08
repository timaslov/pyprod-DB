<template>
  <button
    class="
      rounded-lg
      border-2
      border-black
      hover:bg-amber-500
      duration-300
      h-20
    "
    @click="showTree()"
  >
    <span class="text-xl">{{title}}</span>
  </button>
</template>

<script>
export default {
  name: "subject-block-node",

  props: {
    title: String,
    node: Object
  },

  methods: {
    showTree() {
      this.$emit('showTree', this.node)
    }
  },

}
</script>
