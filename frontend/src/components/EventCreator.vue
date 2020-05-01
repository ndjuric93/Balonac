<template>
<div id="container">
  <b-container fluid>
  <b-row class="justify-content-md-center">
    <b-col md="auto">
      <b-form>
        <label class="sr-only" for="inline-form-input-name">Name</label>
        <b-form-input v-model="location" id="inline-form-input-name" class="mb-1" placeholder="Location" />
        <b-form-datepicker
          v-model="date"
          id="example-datepicker"
          class="mb-1"
        />
        <b-form-timepicker v-model="time" id="example-timepicker" class="mb-3" />
      </b-form>
      </b-col>
    </b-row>
    <b-row>
      <b-col >
        <div>
        <b-table
          hover
          head-variant="light"
          :items="allPlayers"
          :fields="fields"
          responsive="sm"
          sticky-header=300px
          border
        >
          <template v-slot:cell(select_player)="row">
            <b-button size="sm" @click="selectPlayers(row.item)" class="mr-2">
            Select
            </b-button>
          </template>
        </b-table>
        </div>
      </b-col>
      <b-col sm>
        <div>
        <b-table
          striped hover
          :items="eventPlayers"
          :fields="selectedFields"
          sticky-header=300px
        >
          <template v-slot:cell(deselect_player)="row">
            <b-button size="sm" @click="deselectPlayers(row.item)" class="mr-3">
            Deselect
            </b-button>
          </template>
        </b-table>
        </div>
      </b-col>
    </b-row>
    <b-button @click="sendEventCreation" variant="primary">Save</b-button>
  </b-container>
</div>
</template>

<script>
import axios from 'axios'
import getPlayers from '../services/players'

export default {
  name: 'EventCreator',
  data: function () {
    return {
      fields: ['name', 'select_player'],
      selectedFields: ['name', 'deselect_player'],
      eventPlayers: [],
      allPlayers: [],
      location: '',
      date: '',
      time: ''
    }
  },
  created: function () {
    this.fetchPlayers()
  },
  methods: {
    fetchPlayers () {
      getPlayers().then(players => { this.allPlayers = players })
    },
    selectPlayers (selectedPlayer) {
      const playerIndex = this.allPlayers.findIndex(player => selectedPlayer.id === player.id)
      const player = this.allPlayers.splice(playerIndex, 1)
      this.eventPlayers.push(player[0])
    },
    deselectPlayers (deselectedPlayer) {
      const playerIndex = this.eventPlayers.findIndex(player => deselectedPlayer.id === player.id)
      const player = this.eventPlayers.splice(playerIndex, 1)
      this.allPlayers.push(player[0])
      this.allPlayers.sort((a, b) => a.id - b.id)
    },
    sendEventCreation () {
      const players = this.eventPlayers.map(eventPlayer => {
        return {
          player: eventPlayer.id
        }
      })
      axios.post('/v1/event/', {
        location: this.location,
        date: this.date + ' ' + this.time,
        event_player: players
      }).then(response => {
        this.$router.push({ name: 'event', params: { id: response.data.id } })
      })
    }
  }
}
</script>

<style>
#container {
  padding-top: 5%
}
</style>
