<template>
  <div
    id="app"
  >
    <div>
      <Header v-show="isLoggedIn"/>
      <router-view/>
    </div>
  </div>
</template>

<script>
import Header from './components/layout/Header'

export default {
  name: 'App',
  components: {
    Header
  },
  created: function () {
    if (localStorage.getItem('token') !== null) {
      this.$store.commit('setAccessToken', localStorage.getItem('token'))
    }
  },
  methods: {
    isLoggedIn: function () {
      console.log(localStorage.getItem('auth_token') !== '')
      return localStorage.getItem('auth_token') !== ''
    }
  }
}
</script>
