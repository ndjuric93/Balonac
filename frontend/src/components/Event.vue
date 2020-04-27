<template>
<div id="event">
    <h1>{{eventDetails.location}}</h1>
    <h3>{{eventDetails.date}}</h3>
    <h2>Score</h2>
    <h2>{{eventDetails.score_a}} : {{eventDetails.score_b}}</h2>
    <table>
      <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Goals</th>
            <th scope="col">Assists</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(player) in this.teamA" :key=player.id>
          <td>{{player.player_name}}</td>
          <td>{{player.goals_in_game}}</td>
          <td>{{player.assists_in_game}}</td>
        </tr>
      </tbody>
    </table>
    <table>
      <thead>
        <tr>
          <th scope="col">Name</th>
          <th scope="col">Goals</th>
          <th scope="col">Assists</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(player) in this.teamB" :key=player.id>
          <td>{{player.player_name}}</td>
          <td>{{player.goals_in_game}}</td>
          <td>{{player.assists_in_game}}</td>
        </tr>
      </tbody>
    </table>
</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Event',
  props: {
    id: Number
  },
  data: function () {
    return {
      eventDetails: {},
      teamA: [],
      teamB: []
    }
  },
  mounted: function () {
    return axios.get('v1/event/' + this.id)
      .then(response => {
        this.eventDetails = response.data
        this.getTeamA()
        this.getTeamB()
      })
  },
  methods: {
    getTeamA () {
      this.teamA = this.eventDetails.players.filter(player => player.team === '0')
    },
    getTeamB () {
      this.teamB = this.eventDetails.players.filter(player => player.team === '1')
    }
  }
}
</script>

<style scoped>

#event {
  padding-top: 100px;
}

table {
  font-family: 'Open Sans', sans-serif;
  width: auto;
  border-collapse: collapse;
  border: 3px solid rgb(0, 0, 0);
  margin-left: 18%;
  float: left
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
