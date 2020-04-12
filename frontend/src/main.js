import Vue from 'vue'
import Router from 'vue-router'
import App from './App.vue'
import router from './helpers/router'
import store from './helpers/store'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(Router)

axios.defaults.headers.common = {
  Accept: 'application/json',
  'Content-Type': 'application/json'
}
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.interceptors.response.use(function (config) {
  return config
}, function (error) {
  // Prevent endless redirects (login is where you should end up)
  if (error.request !== undefined) {
    if (error.request.responseURL.includes('login')) {
      return Promise.reject(error)
    }
  }

  // If you can't refresh your token or you are sent Unauthorized on any request, logout and go to login
  if (error.request !== undefined && (error.request.responseURL.includes('refresh') || (error.request.status === 401 && error.config.__isRetryRequest))) {
    store.dispatch('logout')
    console.log('IS THIS ALSO HAPPENIGN!!!!?')
  } else if (error.request !== undefined && error.request.status === 401) {
    console.log('PRE ERROR REFRESH???')
    store.dispatch('refresh')
    console.log('POST ERROR REFRESH???')
    error.config.__isRetryRequest = true
    return axios.request(error.config)
  }
  return Promise.reject(error)
})

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
