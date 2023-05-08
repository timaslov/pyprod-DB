import { createRouter, createWebHistory } from 'vue-router'
//import { useAuthStore } from "@/stores/auth.store";

import mainView from "@/views/MainView.vue";
import articlesView from "@/views/ArticlesView.vue";
import aboutView from "@/views/AboutView.vue";
import registrationView from "@/views/RegistrationView.vue";
import authenticationView from "@/views/AuthenticationView.vue";
import articleEditorView from "@/views/ArticleEditorView.vue";
import myArticlesView from "@/views/MyArticlesView.vue";
import articlesToApprove from "@/views/ArticlesToApprove.vue";
import articleToApprove from "@/views/ArticleToApprove.vue";
import empowerUser from "@/views/EmpowerUser.vue";


const routes = [
  {
    path: '/',
    component: mainView
  },
  {
    path: '/about',
    component: aboutView
  },
  {
    path: '/signUp',
    component: registrationView
  },
  {
    path: '/signIn',
    component: authenticationView
  },
  {
    path: '/articles',
    component: articlesView
  },
  {
    path: '/articles/:slug+',
    component: articlesView
  },
  {
    path: '/editor',
    component: articleEditorView
  },
  {
    path: '/editor/:slug+',
    component: articleEditorView
  },
  {
    path: '/myArticles',
    component: myArticlesView
  },
  {
    path: '/articlesToApprove',
    component: articlesToApprove
  },
  {
    path: '/articleToApprove',
    component: articleToApprove
  },
  {
    path: '/empowerUser',
    component: empowerUser
  },
]

const router = createRouter(
    {
      routes,
      history: createWebHistory(import.meta.env.BASE_URL)
    }
)

export default router;

router.beforeEach(async (to) => {
  //const auth = useAuthStore();
  // Использовать useAuthStore или localstorage? И в NavBar тот же вопрос.
  if (localStorage.getItem('user') !== null && (to.fullPath === "/signIn" || to.fullPath === "/signUp")) {
     return '/';
   }
  if (localStorage.getItem('user') === null && (to.fullPath === "/myArticles" ||
                                                    to.fullPath === "/articlesToApprove" ||
                                                    to.fullPath === "/articleToApprove" ||
                                                    to.fullPath === "/empowerUser" ||
                                                    to.fullPath === "/editor")) {
    return '/';
  }
});