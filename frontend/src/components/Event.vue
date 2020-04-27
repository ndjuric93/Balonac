<template>
<div id="event" :style="{'background-image': 'url(' + require('../assets/pastEvent.jpg') + ')'}">
  <div>
    <div id="padding" />
    <b-container id="container">
      <b-row md="justify-content-md-center">
        <b-col  md="4" class="p-3 ">
          <inline-svg
            :src="require('../assets/pastEventLeftPattern.svg')"
            width=80%
          />
        </b-col>
        <b-col md="4" class="ml-auto p-3 ">
          <inline-svg
            :src="require('../assets/pastEventRightPattern.svg')"
            width=80%
          />
        </b-col>
      </b-row>
      <b-row md="justify-content-md-center">
        <b-col >
          <p id="caption">{{this.date}}, ({{this.location}}) </p>
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center">
        <b-col md="auto">
          <p id="caption">Team 1</p>
          <b-table
            hover
            table-variant="light"
            head-variant="light"
            :items="teamA"
            :fields="fields"
            no-border-collapse
            bordered
          >
          </b-table>
        </b-col>
        <b-col md="auto">
          <p id="caption">Team 2</p>
          <b-table
            hover
            table-variant="light"
            head-variant="light"
            :items="teamB"
            :fields="fields"
            no-border-collapse
            bordered
          >
          </b-table>
        </b-col>
      </b-row>
    </b-container>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import InlineSvg from 'vue-inline-svg'

export default {
  name: 'Event',
  components: {
    InlineSvg
  },
  props: {
    id: Number
  },
  data: function () {
    return {
      date: '',
      location: '',
      teamA: [],
      teamB: [],
      fields: [
        { key: 'player_name', label: 'Players', class: 'text-center' },
        { key: 'goals_in_game', label: 'Goals', class: 'text-center' },
        { key: 'assists_in_game', label: 'Assistances', class: 'text-center' }
      ]
    }
  },
  mounted: function () {
    return axios.get('v1/event/' + this.id)
      .then(response => {
        this.date = response.data.date
        this.location = response.data.location
        this.teamA = this.filterTeam(response.data.players, '0')
        this.teamB = this.filterTeam(response.data.players, '1')
      })
  },
  methods: {
    filterTeam (players, team) {
      return players.filter(player => player.team === '0')
    }
  }
}
</script>

<style scoped>

#padding {
  height: 10px
}

#event {
  padding-top: 10%;
  min-height: 100vh;
  background-size: cover;
}

#container {
  background-color: aliceblue;
  max-width: 40%;
  border-radius: 20px;
}

#caption {
  text-align: center;
}

</style>
