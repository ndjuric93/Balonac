<template>
  <div>
    <form class="login" @submit.prevent="login">
      <h1>Balonac</h1>
      <h1>Sign In</h1>
      <label>User name </label><br>
      <input required v-model="username" type="text" placeholder="Enter username">
      <br>
      <label>Password</label><br>
      <input required v-model="password" type="password" placeholder="Enter password">
      <hr/>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data: function () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login: function () {
      this.$store.dispatch('login', {
        username: this.username,
        password: this.password
      })
    }
  }
}
</script>

<style scoped>

</style>
