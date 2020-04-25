<template>
  <div id="playerListContainer" :style="{'background-image': 'url(' + require('../assets/players.jpg') + ')'}">
      <b-container fluid>
        <b-row class="justify-content-md-center">
          <b-col md="auto">
            <b-table
              hover
              table-variant="light"
              head-variant="light"
              :items="players"
              :fields="fields"
              no-border-collapse
              bordered
              sticky-header="80%"
              :sort-by.sync="sortBy"
              :sort-desc.sync="sortDesc"
            >
            </b-table>
          </b-col>
        </b-row>
      </b-container>
  </div>
</template>

<script>
import getPlayers from '../services/players'

export default {
  name: 'PlayerList',
  data: function () {
    return {
      players: [],
      sortDesc: false,
      fields: [
        { key: 'name', sortable: true, class: 'text-center' },
        { key: 'goals', sortable: true, class: 'text-center' },
        { key: 'assists', sortable: true, class: 'text-center' },
        { key: 'won', sortable: true, class: 'text-center' },
        { key: 'lost', sortable: true, class: 'text-center' },
        { key: 'appearances', sortable: true, class: 'text-center' }
      ]
    }
  },
  created: function () {
    getPlayers().then(players => { this.players = players })
  }
}
</script>

<style scoped>

#playerListContainer {
  padding-top: 5%;
  min-height: 100vh;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}

</style>
