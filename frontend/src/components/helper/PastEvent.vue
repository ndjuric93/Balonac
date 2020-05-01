<template>
<div id="event" :style="{'background-image': 'url(' + require('../../assets/pastEvent.jpg') + ')'}">
  <div>
    <div id="padding">
      <Scoreboard
        :team0=this.scoreA
        :team1=this.scoreB
        id="scoreboard"
      />
    </div>
    <b-container id="container">
      <b-row align-h="center">
        <b-col  cols="5">
        </b-col>
      </b-row>
      <b-row md="justify-content-md-center">
        <b-col  md="4" class="p-3 ">
          <inline-svg
            :src="require('../../assets/pastEventLeftPattern.svg')"
            width=80%
          />
        </b-col>
        <b-col md="4" class="ml-auto p-3 ">
          <inline-svg
            :src="require('../../assets/pastEventRightPattern.svg')"
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
import InlineSvg from 'vue-inline-svg'
import Scoreboard from './Scoreboard'

export default {
  name: 'Event',
  components: {
    InlineSvg,
    Scoreboard
  },
  props: ['eventData'],
  data: function () {
    return {
      date: '',
      location: '',
      scoreA: '/',
      scoreB: '/',
      teamA: [],
      teamB: [],
      fields: [
        { key: 'player_name', label: 'Players', class: 'text-center' },
        { key: 'goals_in_game', label: 'Goals', class: 'text-center' },
        { key: 'assists_in_game', label: 'Assistances', class: 'text-center' }
      ]
    }
  },
  created: function () {
    this.date = this.eventData.date
    this.location = this.eventData.location
    this.scoreA = this.eventData.score_a
    this.scoreB = this.eventData.score_b
    this.teamA = this.filterTeam(this.eventData.players, '0')
    this.teamB = this.filterTeam(this.eventData.players, '1')
  },
  methods: {
    filterTeam (players, team) {
      return players.filter(player => player.team === team)
    }
  }
}
</script>

<style scoped>

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

#padding {
  position: absolute;
  left: 43%;
}

#scoreboard {
  margin-top: -45px;
}

</style>
