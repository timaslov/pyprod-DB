<template>
  <div id="app" class="relative min-h-screen font-sans">
    <nav-bar/>

    <div class="pb-[80px]">
      <router-view/>
    </div>

    <footer-component/>
  </div>
</template>

<script>
import navBar from "@/components/NavBar.vue";
import FooterComponent from"@/components/Footer.vue";
export default {
  components: {
    navBar,
    FooterComponent
  }
}
</script>
