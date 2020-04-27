import axios from 'axios'

export default {
  state: {
    access: '',
    refresh: ''
  },
  getters: {
    loggedIn (state) {
      return !!state.access
    }
  },
  mutations: {
    setRefreshToken (state, token) {
      state.refresh = token
    },
    setAccessToken (state, token) {
      state.access = token
      axios.defaults.headers.Authorization = 'Bearer ' + token
      localStorage.setItem('token', state.access)
    },
    clearTokens (state) {
      state.access = ''
      state.refresh = ''
      localStorage.removeItem('token')
    }
  },
  actions: {
    LOGIN: ({ commit }, payload) => {
      return new Promise((resolve, reject) => {
        axios.post('token/', payload)
          .then(response => {
            if (response.status === 200) {
              commit('setAccessToken', response.data.access)
              commit('setRefreshToken', response.data.refresh)
              resolve(true)
            }
          })
          .catch(error => {
            reject(error)
          })
      })
    },
    REFRESH: ({ commit }) => {
      return new Promise((resolve, reject) => {
        axios
          .post('token/refresh/')
          .then(response => {
            commit('setAccessToken', {
              access: response.access
            })
            resolve(response)
          })
          .catch(error => {
            reject(error)
          })
      })
    },
    LOGOUT: ({ commit }) => {
      return new Promise(resolve => {
        commit('clearTokens')
        resolve(true)
      })
    }
  }
}
