<template>
  <div class="main">
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>
    <router-link to="/events/create" tag="button">Napravi novi termin</router-link><br>
    <router-link to="/events" tag="button">Pogledaj sve termine</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'MainPage',
  props: {
    title: String,
    description: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
