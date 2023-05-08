<template>
  <div>
    <div
      class="p-2 inline-flex space-x-3 items-end"
      :style="{'margin-left': `${depth * 20}px`}"
    >
      <tree-leaf
        @click="chooseArticle()"
        :node="node"
        :path-array="this.pathArray"
      />

      <span
        class="text-amber-600 cursor-pointer"
        v-if="ifChildrenExist()"
        @click="expanded = !expanded"
      >
        {{expanded ? '&#9660;' : '&#10148;'}}
      </span>
    </div>

    <TreeBrowser
      v-if="expanded"
      v-for="child in node.children"
        :key="child.name"
        :node="child"
        :depth="depth + 1"
        :path-array="this.pathArray.slice(1)"
      @changeArticle="sendArtID($event)"
    />
  </div>
</template>

<script>
import treeLeaf from "@/components/TreeLeaf.vue";
export default {
  components: {treeLeaf},

  name: 'TreeBrowser',

  props: {
    node: Object,
    pathArray: Array,
    depth: {
      type: Number,
      default: 0,
    },
  },

  data() {
    return {
      expanded: false,
      nextArray: Array,
    }
  },

  methods: {
    chooseArticle() {
        this.$emit('changeArticle', this.node)
    },
    sendArtID(node) {
      this.$emit('changeArticle', node)
    },
    ifChildrenExist() {
      return this.node.children.length > 0;
    }
  },

  mounted() {
    if (this.pathArray[0] === this.node.slug && this.pathArray.length > 1)
    {
      this.expanded = true
    }
  },

}
</script>
