<script setup>
import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';

const schema = Yup.object().shape({
  email: Yup.string().required('Email is required')
});
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
      <h1 class="text-center text-2xl">Наделение правами модератора</h1>

      <div class="grid grid-cols-2 place-items-center">
        <label>email</label>
        <Field name="email" class="border-2" />
        <div v-if="errors.email" class="text-red-500">{{ 'Введите email' }}</div>
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
        >Сделать модератором</button>
      </div>

      <div v-if="errors.apiError" class="text-red-500">{{errors.apiError}}</div>
    </Form>
  </div>
</template>

<script>
import axios from "axios";
import {useAuthStore} from "../stores/auth.store";
export default {
  name: "EmpowerUser",

  methods: {
    async onSubmit(values, { setErrors }) {
      console.log(values)

      const authStore = useAuthStore();
      let response
      let token = authStore.user.access
      let body = {email: values.email, is_staff: "True"};
      let config = {headers: { Authorization: `Bearer ${token}` }};

      try {
        response = await axios.post(
            "http://localhost:8001/api/web/v1/users/set_permission_level/", body, config)
      } catch(error)
      {
        switch (error.response.status){
          case 401:
            throw 'Ошибка 401'
          default:
            throw error.response.status
        }
      }
      console.log(response)

    }
  }
}
</script>
