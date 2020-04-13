<template>
<div>
  <b-container fluid>
  <b-row class="justify-content-md-center">
    <b-col md="auto">
      <b-form inline>
        <label class="sr-only" for="inline-form-input-name">Name</label>
        <b-input id="inline-form-input-name" class="mb-1" placeholder="Location" />
        <b-form-datepicker id="example-datepicker" class="mb-1" />
        <b-form-timepicker id="example-datepicker" class="mb-1" />
      </b-form>
      </b-col>
    </b-row>
    <b-row>
      <b-col >
        <b-table hover :items="allPlayers" :fields="fields" responsive="sm">
          <template v-slot:cell(select_player)="row">
            <b-button size="sm" @click="selectPlayers(row.item.id)" class="mr-2">
              Select
            </b-button>
          </template>
        </b-table>
      </b-col>
      <b-col sm>
        <b-table striped hover :items="eventPlayers" :fields="selectedFields">
          <template v-slot:cell(deselect_player)="row">
            <b-button size="sm" @click="deselectPlayers(row.item.id)" class="mr-3">
              Deselect
            </b-button>
          </template>
        </b-table>
      </b-col>
    </b-row>
      <b-button variant="primary">Save</b-button>

  </b-container>
</div>
</template>

<script>
import getPlayers from '../helpers/players'
export default {
  name: 'EventCreator',
  data: function () {
    return {
      fields: ['name', 'select_player'],
      selectedFields: ['name', 'deselect_player'],
      eventPlayers: [],
      allPlayers: []
    }
  },
  created: function () {
    this.fetchPlayers()
  },
  methods: {
    fetchPlayers () {
      getPlayers().then(players => { this.allPlayers = players })
    },
    selectPlayers (playerId) {
      console.log(playerId)
      this.eventPlayers.push(this.allPlayers[playerId])
      this.allPlayers.splice(playerId, 1)
    },
    deselectPlayers (playerId) {
      this.allPlayers.push(this.eventPlayers[playerId])
      this.eventPlayers.splice(playerId, 1)
    },
    sendEventCreation () {
      console.log('Sending out an SOS')
    }
  }
}
</script>

<style>

</style>
