<template>
<div>
</div>
</template>
<script>
export default {
  name: 'Logout',
  created: function () {
    this.$store.dispatch('LOGOUT')
    this.$router.push('/login')
  }
}
</script>
