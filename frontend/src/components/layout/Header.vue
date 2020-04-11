<template>
  <b-navbar fixed="top" type="dark" variant="dark">
    <b-navbar-brand>
    Balonac
    </b-navbar-brand>
    <div id="nav">
      <b-navbar-nav>
        <router-link to="/" tag="b-nav-item">Home</router-link>
        <router-link to="/players" tag="b-nav-item">Players</router-link>
        <router-link to="/events" tag="b-nav-item">Events</router-link>
        <router-link to="/logout" tag="b-nav-item">Logout</router-link>
      </b-navbar-nav>
    </div>
  </b-navbar>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style scoped>
  .header {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 10px;
  }
  .header a {
    color: #fff;
    padding-right: 5px;
    text-decoration: none;
  }
</style>
