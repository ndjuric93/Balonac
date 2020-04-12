import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import router from './router'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    token: localStorage.getItem('auth_token') || '',
    refreshToken: localStorage.getItem('refresh_token') || ''
  },
  mutations: { // Sync
    refresh (state) {
      axios.post(process.env.VUE_APP_BASE_URL + 'api/token/refresh',
        {
          refresh: localStorage.getItem('refresh_token')
        }).then(response => {
        state.token = response.data.access
        localStorage.setItem('auth_token', response.data.access)
        axios.defaults.headers.common.Authorization = 'Bearer ' + response.data.access
      })
    }
  },
  actions: { // Async
    login (state, user) {
      axios.post(process.env.VUE_APP_BASE_URL + 'api/token/',
        {
          username: user.username,
          password: user.password
        }).then(response => {
        const token = response.data.access
        const refreshToken = response.data.refresh
        console.log(refreshToken)
        localStorage.setItem('auth_token', token)
        localStorage.setItem('refresh_token', refreshToken)
        state.token = token
        state.refreshToken = refreshToken
        axios.defaults.headers.common.Authorization = 'Bearer ' + token
        router.push('/')
      }).catch(err => {
        console.log(err)
        localStorage.removeItem('auth_token')
      })
    },
    logout (state) {
      state.token = ''
      localStorage.removeItem('auth_token')
    }
  },
  getters: {
  }
})

export default store
