<template>
  <div class="main">
    <h1>This is list of all players</h1>
    <table>
        <thead>
          <tr>
            <th scope="col">Name</th>
            <th scope="col">Goals</th>
            <th scope="col">Assists</th>
            <th scope="col">Apps</th>
            <th scope="col">Won</th>
            <th scope="col">Lost</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(player) in players" :key="player.id">
                <td>{{player.name}}</td>
                <td>{{player.goals}}</td>
                <td>{{player.assists}}</td>
                <td>{{player.appearances}}</td>
                <td>{{player.won}}</td>
                <td>{{player.lost}}</td>
          </tr>
        </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'PlayerList',
  data: function () {
    return {
      players: []
    }
  },
  created: function () {
    this.fetchPlayers()
  },
  methods: {
    fetchPlayers () {
      return axios.get('http://localhost:8000/v1/player')
        .then(response => {
          console.log(response.data)
          this.players = response.data
        }).catch(e => {
          console.log(e)
        })
    }
  }
}
</script>

<style scoped>

table {
  font-family: 'Open Sans', sans-serif;
  width: auto;
  border-collapse: collapse;
  border: 3px solid rgb(0, 0, 0);
  margin-left: auto;
  margin-right: auto;

}

table th {
  text-transform: uppercase;
  text-align: left;
  background: rgb(0, 0, 0);
  color: #FFF;
  padding: 8px;
  min-width: 30px;
}

table td {
  text-align: left;
  padding: 8px;
  border-right: 2px solid rgb(0, 0, 0);
}
table td:last-child {
  border-right: none;
}
table tbody tr:nth-child(2n) td {
  background: #D4D8F9;
}

</style>
