<template>
  <div class="main">
    <h1>This is a list of all the events</h1>
    <table>
      <thead>
        <tr>
          <th scope="col">Date</th>
          <th scope="col">Location</th>
          <th scope="col">Player Count</th>
          <th scope="col">Score</th>
          <th scope="col">Completed</th>
          <th scope="col">Explore</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(event) in events" :key="event">
          <td>{{event.date}}</td>
          <td>{{event.location}}</td>
          <td>{{event.players.length}}</td>
          <td>{{event.score_a + ':' + event.score_b}}</td>
          <td>{{event.completed}}</td>
          <td>
            <router-link to="/players" tag="button">Details</router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'EventList',
  data: function () {
    return {
      events: []
    }
  },
  created: function () {
    this.fetchEvents()
  },
  methods: {
    fetchEvents () {
      return axios.get('http://ec2-13-59-63-162.us-east-2.compute.amazonaws.com/v1/event')
        .then(response => {
          this.events = response.data
        }).catch(e => {
          this.errors.push(e)
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
