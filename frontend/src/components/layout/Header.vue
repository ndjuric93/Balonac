<template>
  <b-navbar fixed="top" id="navBar" toggleable="sm" v-show="loggedIn">

    <b-navbar-brand href="#" class="d-inline-block align-top" to="/">
      <img src='../../assets/balloon-01-01.png' alt="Balonac">
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>

    <b-navbar-nav class="ml-auto">
      <b-nav-item to="/players">
        <b-nav-text id="navItem">
          PLAYERS
        </b-nav-text>
      </b-nav-item>
      <b-nav-item to="/events">
        <b-nav-text id="navItem">
          EVENTS
        </b-nav-text>
      </b-nav-item>
      <b-nav-item  to="/logout">
        <b-nav-text id="navItem">
          LOGOUT
        </b-nav-text>
      </b-nav-item>
    </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
import { authComputed } from '../../helpers/vuex'

export default {
  name: 'Header',
  methods: {
    isLoggedIn: function () {
      return localStorage.getItem('auth_token') !== ''
    }
  },
  computed: {
    ...authComputed
  }
}
</script>

<style scoped>
  #navBar {
    background-color: #0c3c65;
  }

  #navItem {
    color: white;
    font-size: 20px;
  }
</style>
