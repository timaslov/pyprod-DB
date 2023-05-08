<script setup>
import { Form, Field } from 'vee-validate';
import { useAuthStore } from '@/stores/auth.store';
import * as Yup from 'yup';

const schema = Yup.object().shape({
  username: Yup.string().required('Username is required'),
  password: Yup.string().required('Password is required')
});
function onSubmit(values, { setErrors }) {
  const authStore = useAuthStore();
  const { username, password } = values;

  return authStore.login(username, password)
      .catch(error => setErrors({apiError: error}));
}
</script>

<template>
  <div class="flex flex-col p-10 place-items-center">
    <Form
      @submit="onSubmit"
      :validation-schema="schema"
      v-slot="{errors, isSubmitting}"
      class="
        flex
        flex-col
        space-y-10
        place-items-center
        p-10 border-2
        border-black
        w-[400px]
      "
    >
      <h1 class="text-center text-2xl">Вход</h1>

      <div class="grid grid-cols-2 place-items-center">
        <label>Логин / Email</label>
        <Field name="username" class="border-2" />
        <div v-if="errors.username" class="text-red-500">{{ 'Введите логин' }}</div>
      </div>

      <div class="grid grid-cols-2 place-items-center">
        <label>Пароль</label>
        <Field name="password" type="password" class="border-2" />
        <div v-if="errors.password" class="text-red-500">{{ 'Введите пароль' }}</div>
      </div>

      <div>
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
              "
        >Войти</button>
      </div>

      <div v-if="errors.apiError" class="text-red-500">{{errors.apiError}}</div>

    </Form>

    <div class="m-5">
      <h1 class="text-center text-2xl">Еще нет аккаунта?</h1>
        <router-link to="/signUp">
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
              m-5
            "
          >
            Зарегистрироваться
          </button>
        </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "authentication-view",
}
</script>
