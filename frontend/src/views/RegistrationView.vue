<script setup>
import { Form, Field } from 'vee-validate';
import { useAuthStore } from '@/stores/auth.store';
import * as Yup from 'yup';
import axios from "axios";

const schema = Yup.object().shape({
  firstname: Yup.string().required('Firstname is required'),
  lastname: Yup.string().required('Lastname is required'),
  username: Yup.string().required('Username is required'),
  email: Yup.string().required('Email is required'),
  password: Yup.string().required('Password is required')
});
async function onSubmit(values, { setErrors }) {
  console.log(values)

  let response
  let body = {first_name: values.firstname, last_name: values.lastname, username: values.username, email: values.email, password: values.password};
  console.log(body)
  try {
    response = await axios.post(
        "http://localhost:8001/api/web/v1/users/register/", body)
  } catch(error)
  {
    switch (error.response.status){
      case 401:
        throw 'Ошибка 401'
      default:
        throw error.response.status
    }
  }

}
</script>

<template>
  <div class="flex flex-col p-10 place-items-center" >
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
      <h1 class="text-center text-2xl">Регистрация</h1>

      <div class="grid grid-cols-2 place-items-center">
        <label>Имя</label>
        <Field name="firstname" class="border-2" />
        <div v-if="errors.username" class="text-red-500">{{ 'Введите firstname' }}</div>
      </div>

      <div class="grid grid-cols-2 place-items-center">
        <label>Фамилия</label>
        <Field name="lastname" class="border-2" />
        <div v-if="errors.username" class="text-red-500">{{ 'Введите lastname' }}</div>
      </div>

      <div class="grid grid-cols-2 place-items-center">
        <label>Имя польз.</label>
        <Field name="username" class="border-2" />
        <div v-if="errors.username" class="text-red-500">{{ 'Введите username' }}</div>
      </div>

      <div class="grid grid-cols-2 place-items-center">
        <label>Email</label>
        <Field name="email" class="border-2" />
        <div v-if="errors.username" class="text-red-500">{{ 'Введите email' }}</div>
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
        >Зарегистрироваться</button>
      </div>

      <div v-if="errors.apiError" class="text-red-500">{{errors.apiError}}</div>

    </Form>
  </div>
</template>

<script>
export default {
  name: "registration-view"
}
</script>
