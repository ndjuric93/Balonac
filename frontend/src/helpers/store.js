import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import router from './router'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    token: localStorage.getItem('auth_token') || ''
  },
  mutations: { // Sync
  },
  actions: { // Async
    login (state, user) {
      axios.post('http://localhost:8000/api/token/',
        {
          username: user.username,
          password: user.password
        }).then(response => {
        const token = response.data.access
        localStorage.setItem('auth_token', token)
        state.token = token
        axios.defaults.headers.common.Authorization = 'Bearer ' + token
        router.push('/')
      }).catch(err => {
        localStorage.removeItem('auth_token')
        console.log(err)
      })
    },
    logout (state) {
      console.log('ThiS HAPPENS')
      state.token = ''
      localStorage.removeItem('auth_token')
    }
  },
  getters: {
  }
})

export default store
