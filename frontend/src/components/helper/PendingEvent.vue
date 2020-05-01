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
            <template v-slot:cell(actions)="row">
              <div id="center">
                <b-button
                  @click="registerAction(row)"
                >
                  {{state}}
                </b-button>
              </div>
            </template>
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
            <template v-slot:cell(actions)="row">
                <b-button
                  @click="registerAction(row)"
                  v-show="row.item.isActive"
                >
                  {{state}}
                </b-button>
            </template>
          </b-table>
        </b-col>
      </b-row>
      <b-row md="justify-content-md-center">
        <b-col>
          <div>
          <b-button pill block v-on:click="finishEvent">
            FINISH EVENT
          </b-button>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</div>
</template>

<script>
import axios from 'axios'

import InlineSvg from 'vue-inline-svg'
import Scoreboard from './Scoreboard'

export default {
  name: 'Event',
  components: {
    InlineSvg,
    Scoreboard
  },
  props: ['eventData', 'eventId'],
  data: function () {
    return {
      date: '',
      location: '',
      scoreA: '/',
      scoreB: '/',
      teamA: [],
      teamB: [],
      state: 'GOAL!',
      goalData: {},
      fields: [
        { key: 'player_name', label: 'Players', class: 'text-center' },
        { key: 'goals_in_game', label: 'Goals', class: 'text-center' },
        { key: 'assists_in_game', label: 'Assistances', class: 'text-center' },
        { key: 'actions', label: 'Actions', class: 'text-center' }
      ]
    }
  },
  created: function () {
    this.date = this.eventData.date
    this.location = this.eventData.location
    this.teamA = this.filterTeam(this.eventData.players, '0')
    this.teamB = this.filterTeam(this.eventData.players, '1')
    this.scoreA = this.teamA.map(player => player.goals_in_game).reduce((a, b) => a + b, 0)
    this.scoreB = this.teamB.map(player => player.goals_in_game).reduce((a, b) => a + b, 0)
  },
  methods: {
    filterTeam (players, team) {
      players.map(player => { player.isActive = true })
      return players.filter(player => player.team === team)
    },
    registerAction (row) {
      if (this.state === 'GOAL!') {
        this.goalAction(row)
      } else {
        this.assistAction(row)
      }
    },
    goalAction (row) {
      this.goalData.scorer = row.item.id
      const players = row.item.team === '0' ? this.teamB : this.teamA
      players.map(player => { player.isActive = false })
      this.state = this.state === 'GOAL!' ? 'ASSIST!' : 'GOAL!'
    },
    assistAction (row) {
      this.goalData.assistant = row.item.id
      this.completeAction()
    },
    completeAction () {
      axios.put('/v1/event/player/' + this.goalData.scorer + '/', {
        assistant_id: this.goalData.assistant
      }).then(() => {
        this.refreshPlayers()
        this.state = 'GOAL!'
        this.$router.go()
      })
    },
    refreshPlayers () {
      this.teamA.map(player => { player.isActive = true })
      this.teamB.map(player => { player.isActive = true })
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
  max-width: 50%;
  border-radius: 20px;
  padding: 3%;
}

#caption {
  text-align: center;
}

#padding {
  position: absolute;
  left: 45%;
}

#scoreboard {
  margin-top: -45px;
}

</style>
