import { defineStore } from 'pinia';
import router from "@/router";
import axios from "axios";

export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        user: JSON.parse(localStorage.getItem('user')),
    }),

    actions: {
        async login(email, password) {
            let response
            try {
                response = await axios.post(
                    "http://localhost:8001/api/web/v1/users/token/",
                    {email: email, password: password})
            } catch(error)
            {
                switch (error.response.status){
                    case 401:
                        throw 'Неправильный логин или пароль'
                    default:
                        throw error.response.status
                }
            }

            response.data.email = email;
            this.user = response.data;
            localStorage.setItem('user', JSON.stringify(response.data));

            await router.push('/');
        },

        logout() {
            this.user = null;
            localStorage.removeItem('user');
        }
    }
});
