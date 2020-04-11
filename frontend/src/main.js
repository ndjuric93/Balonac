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

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
