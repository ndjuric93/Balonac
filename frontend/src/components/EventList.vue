<template>
  <div class="main">
    <h1>This is event list</h1>
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>
  </div>
</template>

<script>

export default {
  name: 'EventList',
  props: {
    title: String,
    description: String
  }
}
</script>

<style scoped>
</style>
