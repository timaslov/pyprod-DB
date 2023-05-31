import { defineStore } from 'pinia';
import router from "@/router";
import axios from "axios";

export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        user: JSON.parse(localStorage.getItem('user')),
        userInfo: JSON.parse(localStorage.getItem('userInfo')),
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
            console.log(response)
            response.data.email = email;
            this.user = response.data;
            localStorage.setItem('user', JSON.stringify(response.data));

            let token = this.user.access
            let config = {headers: { Authorization: `Bearer ${token}` }};

            try {
                response = await axios.get(
                    "http://localhost:8001/api/web/v1/users/", config)
            } catch(error)
            {
                switch (error.response.status){
                    case 401:
                        throw 'Ошибка 401'
                    default:
                        throw error.response.status
                }
            }
            this.userInfo = response.data;
            localStorage.setItem('userInfo', JSON.stringify(response.data));

            await router.push('/');
        },

        logout() {
            this.user = null;
            localStorage.removeItem('user');
            this.userInfo = null;
            localStorage.removeItem('userInfo');
        }
    }
});
