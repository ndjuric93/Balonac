<template>
<div>
</div>
</template>
<script>
export default {
  name: 'Logout',
  data: function () {
    return {}
  },
  created: function () {
    this.$store.dispatch('logout')
    this.$router.push('/login')
  }
}
</script>
