<script setup>
import { useAuthStore } from '@/stores/auth.store';
const authStore = useAuthStore();
</script>

<template>
  <nav
    class="
      h-[70px]
      min-w-[200px]
      bg-gray-300
    "
  >
    <div
      class="
        container
        flex
        items-center
        justify-between
        mx-auto
        h-full
      "
    >
      <!-- Логотип и надпись слева в широком режиме -->
      <router-link
        to="/"
        class="
          hidden
          md:flex
          space-x-2
          items-center
          min-w-[50px]
          w-[142px]
        "
      >
        <img
          src="@/assets/cube_logo.png"
          alt="logo"
          class="h-[50px] mx-auto"
        >
        <span
          class="text-2xl text-amber-700"
        >
          PyProd
        </span>
      </router-link>

      <!-- Кнопка выпадающего меню слева в сжатом режиме -->
      <div
        class="
          w-[150px]
          md:hidden
        "
      >
        <button
        id="navMenuButton"
        type="button"
        class="
          mx-3
          w-[50px] h-[50px]
          text-sm
          text-gray-500
        "
        @click="toggleNavMenu()"
        >
          <svg
            id="navMenuButtonSVG"
            class="w-10 h-10 m-auto hover:bg-gray-100 rounded-lg"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path
              id="navMenuButtonSVGPath"
              fill-rule="evenodd"
              d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1
                1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
              clip-rule="evenodd"
            >
            </path>
          </svg>
        </button>
      </div>

      <!-- Навигационное меню для обоих режимов -->
      <div
        id="navMenu"
        class="
          md:flex
          md:w-auto
          w-[150px]
          z-50
        "
        @click="closeNavMenu()"
        v-bind:class="{'hidden': !showNavMenu, 'absolute pt-[250px]': showNavMenu}"
      >
        <ul
          class="
            flex
            flex-col
            p-4
            rounded-lg
            bg-gray-300
            md:flex-row
            md:space-x-8
            md:text-sm
            md:font-medium
            md:bg-white
          "
        >
          <li>
            <router-link
              to="/articles"
              class="
                block py-2 pl-3 pr-4 rounded
                md:bg-transparent
                md:p-0
                md:hover:bg-transparent
                md:hover:text-amber-600
                hover:bg-amber-600
                hover:text-white
              "
              :class="{
                'md:text-amber-600 bg-amber-600 text-white' : this.curTab === 'articles',
                'md:text-gray-700' : this.curTab !== 'articles',
              }"
            >
              Статьи
            </router-link>
          </li>

          <li>
            <router-link
                to="/about"
                class="
                block py-2 pl-3 pr-4 rounded
                md:bg-transparent
                md:p-0
                md:hover:bg-transparent
                md:hover:text-amber-600
                hover:bg-amber-600
                hover:text-white
              "
                :class="{
                'md:text-amber-600 bg-amber-600 text-white' : this.curTab === 'about',
                'md:text-gray-700' : this.curTab !== 'about',
              }"
            >
              О проекте
            </router-link>
          </li>



          <li>
            <p
              class="
                block py-2 pl-3 pr-4 rounded
                md:bg-transparent
                md:text-gray-700
                md:p-0
                md:hover:bg-transparent
                md:hover:text-amber-600
                hover:bg-amber-600
                hover:text-white
              "
            >
              {{ "Поиск" }}
            </p>
          </li>
        </ul>
      </div>

      <!-- Логотип по центру в сжатом режиме -->
      <router-link
        to="/"
        class="
          flex
          md:hidden
          items-center
          w-[60px]
          min-w-[60px]
        "
      >
        <img
          src="@/assets/cube_logo.png"
          alt="logo"
          class="h-[50px]"
        >
      </router-link>

      <div class="w-[150px]">
        <!-- Кнопка "Войти" справа в широком режиме -->
        <div
          class="
            hidden
            md:flex
          "
        >
          <router-link
            to="/signIn"
            v-if="authStore.user === null"
            class="mx-auto"
          >
            <button
              type="button"
              class="
                text-white
                bg-amber-600
                hover:bg-amber-800
                duration-300
                font-medium
                rounded-lg
                text-sm
                px-5
                py-2.5
              "
            >
              Войти
            </button>
          </router-link>
        </div>

        <!-- Иконка "Аккаунт" справа в широком режиме -->
        <div class="hidden md:block">
          <button
              id="accountIcoBigButton"
              @click="accountButtonClick"
              v-if="authStore.user !== null"
              class="
              flex
              mx-auto
              w-[50px] h-[50px]
              hover:border-2
              border-gray-600
              rounded-full
              cursor-pointer
            "
          >
            <div
                class="
                m-auto
                relative
                w-10 h-10
                overflow-hidden
                bg-gray-100
                rounded-full
              "
            >
              <svg
                  id="accountIcoBigSVG"
                  class="absolute w-12 h-12 text-gray-400 -left-1"
                  fill="currentColor"
                  viewBox="0 0 20 20"
              >
                <path
                    id="accountIcoBigSVGPath"
                    fill-rule="evenodd"
                    d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
                    clip-rule="evenodd"
                >
                </path>
              </svg>
            </div>
          </button>

          <nav-bar-user-menu v-if="showUserMenu"/>
        </div>

        <!-- Иконка "Войти" справа в сжатом режиме -->
        <router-link
          v-if="authStore.user === null"
          to="/signIn"
          class="
            w-[50px] h-[50px]
            flex
            md:hidden
            mr-3 ml-auto
          "
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-log-in mx-auto my-auto text-gray-500" id="IconChangeColor"><path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4" id="mainIconPathAttribute"></path><polyline points="10 17 15 12 10 7"></polyline><line x1="15" y1="12" x2="3" y2="12"></line></svg>
        </router-link>

        <!-- Иконка "Аккаунт" справа в сжатом режиме -->
        <div class="block md:hidden">
          <button
              id="accountIcoSmallButton"
              @click="accountButtonClick"
              v-if="authStore.user !== null"
              class="
              flex
              mr-3 ml-auto
              w-[50px] h-[50px]
              hover:border-2
              border-gray-600
              rounded-full
              cursor-pointer
            "
          >
            <div
                class="
                m-auto
                relative
                w-10 h-10
                overflow-hidden
                bg-gray-100
                rounded-full
              "
            >
              <svg
                  id="accountIcoSmallSVG"
                  class="absolute w-12 h-12 text-gray-400 -left-1"
                  fill="currentColor"
                  viewBox="0 0 20 20"
              >
                <path
                    id="accountIcoSmallSVGPath"
                    fill-rule="evenodd"
                    d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
                    clip-rule="evenodd"
                >
                </path>
              </svg>
            </div>
          </button>

          <nav-bar-user-menu v-if="showUserMenu"/>
        </div>
      </div>

    </div>
  </nav>
</template>

<script>
import navBarUserMenu from "@/components/NavBarUserMenu.vue";
export default {
  name: "nav-bar",

  components: {navBarUserMenu},

  data() {
    return {
      curTab: String,
      showNavMenu: false,
      showUserMenu: false,
    }
  },

  created() {
    window.addEventListener("resize", this.resizeHandler);
    window.addEventListener("click", this.clickHandler);
  },

  destroyed() {
    window.removeEventListener("resize", this.resizeHandler);
    window.addEventListener("click", this.clickHandler);
  },

  methods: {
    toggleNavMenu: function(){
      this.showNavMenu = !this.showNavMenu;
    },

    closeNavMenu: function(){
      this.showNavMenu = false;
    },

    resizeHandler() {
      this.closeNavMenu();
    },

    clickHandler(e) {
      // Лютые костыли, который надо поправить
      if (e.target.id !== 'navMenuButton' &&
          e.target.id !== 'navMenuButtonSVG' &&
          e.target.id !== 'navMenuButtonSVGPath')
        this.closeNavMenu();

      if (e.target.id !== 'accountIcoBigSVG' &&
          e.target.id !== 'accountIcoBigSVGPath' &&
          e.target.id !== 'accountIcoBigButton' &&
          e.target.id !== 'accountIcoSmallButton' &&
          e.target.id !== 'accountIcoSmallSVG' &&
          e.target.id !== 'accountIcoSmallSVGPath')
        this.closeUserMenu();

    },

    accountButtonClick() {
      this.toggleUserMenu()
    },

    toggleUserMenu: function(){
      this.showUserMenu = !this.showUserMenu;
    },

    closeUserMenu: function(){
      this.showUserMenu = false;
    },

  },

  watch: {
    $route: function () {
      this.curTab = this.$route.path.split('/')[1];
    },
  },

}
</script>
