import Vue from 'vue'
import Router from 'vue-router'
import App from './App.vue'
import router from './services/router'
import store from './stores/store'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(Router)

axios.defaults.baseURL = process.env.VUE_APP_BASE_URL
axios.defaults.withCredentials = true
axios.interceptors.response.use(
  response => response,
  error => {
    if (error.response.status === 401) {
      store.dispatch('LOGOUT')
    }
    return Promise.reject(error)
  }
)

axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  const originalRequest = error.config
  if (error.response.status === 401) {
    originalRequest._retry = true
    store.commit('refresh')
    originalRequest.headers.Authorization = 'Bearer ' + localStorage.getItem('auth_token')
    return axios(originalRequest)
  }
  return Promise.reject(error)
})

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
