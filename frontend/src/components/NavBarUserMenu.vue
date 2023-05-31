<script setup>
import { useAuthStore } from '@/stores/auth.store';
const authStore = useAuthStore();

function logoutButton() {
  authStore.logout();
}
</script>
<template>
  <!-- Меню пользователя-->
  <div
    class="
      z-50
      absolute
      w-[150px]
    "
  >
    <ul
      class="
        flex
        flex-col
        py-2
        rounded-lg
        bg-gray-300
        mr-0
        ml-auto
      "
    >
      <li v-if="this.isStaff || this.isSuperUser">
        <router-link
          to="/editor"
          class="
            w-full
            block py-2 pl-3 pr-4 rounded
            hover:bg-amber-600
            hover:text-white
            text-center
          "
        >
          Новая статья
        </router-link>
      </li>

      <li v-if="this.isStaff || this.isSuperUser">
        <router-link
            to="/myArticles"
            class="
            w-full
            block py-2 pl-3 pr-4 rounded
            hover:bg-amber-600
            hover:text-white
            text-center
          "
        >
          Мои статьи
        </router-link>
      </li>

      <li v-if="this.isSuperUser">
        <router-link
            to="/articlesToApprove"
            class="
            w-full
            block py-2 pl-3 pr-4 rounded
            hover:bg-amber-600
            hover:text-white
            text-center
          "
        >
          Статьи к проверке
        </router-link>
      </li>

      <li v-if="this.isSuperUser">
        <router-link
            to="/empowerUser"
            class="
            w-full
            block py-2 pl-3 pr-4 rounded
            hover:bg-amber-600
            hover:text-white
            text-center
          "
        >
          Наделить правами
        </router-link>
      </li>

      <li>
        <router-link to="/">
          <button
            @click="logoutButton"
            class="
              w-full
              block py-2 pl-3 pr-4 rounded
              hover:bg-amber-600
              hover:text-white
            "
          >
            Выйти
          </button>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "NavBarUserMenu",
  data() {
    return {
      isSuperUser: false,
      isStaff: false,
    }
  },

  async created() {
    const authStore = useAuthStore();
    console.log(authStore.userInfo)
    this.isStaff = authStore.userInfo.is_staff
    this.isSuperUser = authStore.userInfo.is_superuser
  }
}
</script>

<style scoped>

</style>