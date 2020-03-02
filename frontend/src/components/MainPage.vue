<template>
  <div class="main">
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>
    <button>Dodaj novi termin</button><br>
    <button>Pogledaj sve termine</button>
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
