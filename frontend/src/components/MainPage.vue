<template>
  <div id="mainPageContainer" :style="{'background-image': 'url(' + require('../assets/main_page.jpg') + ')'}">
    <b-container class="bv-example-row bv-example-row-flex-cols">
      <b-row align-h="start">
        <b-col cols="6">
          <router-link to="/events/create" tag="p">
            <b-card
              border-variant="secondary"
              header-border-variant="secondary"
              align="center"
              id="eventCard"
            >
              <img id="makeEventButton" src="../assets/more.svg" />
              <h3 id="newEventText">MAKE NEW EVENT</h3>
            </b-card>
          </router-link>
        </b-col>
      </b-row>
      <b-row align-v="center" align-h="center" id="bottomRow">
        <b-col cols="6">
          <div id="cardSize">
            <b-card
              border-variant="secondary"
              header="Upcoming events"
              header-border-variant="secondary"
              align="center"
              style="min-height: 200px"
            >
              <b-card-text>Corona time baby. No upcoming events :(</b-card-text>
            </b-card>
          </div>
        </b-col>
        <b-col cols="6">
          <div id="cardSize">
            <b-card
              border-variant="secondary"
              header="Top Players"
              header-border-variant="secondary"
              align="center"
              footer-bg-variant="success"
              footer-border-variant="dark"
              style="min-height: 200px"
            >
              <b-card-text id="playerCardText" v-for="(player, index) in topPlayers" :key="player.id">
                {{index + 1}}. {{player.name}} - {{player.goals}} goals - {{player.assists}} assists
              </b-card-text>
            </b-card>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import getPlayers from '../services/players'

export default {
  name: 'MainPage',
  data: function () {
    return {
      topPlayers: []
    }
  },
  mounted: function () {
    this.getTopPlayers()
  },
  methods: {
    getTopPlayers: function () {
      return getPlayers().then(players => {
        players.sort((playerA, playerB) => {
          return ((playerA.goals + playerA.assists) < (playerB.goals + playerB.assists)) ? 1 : -1
        })
        this.topPlayers = players.slice(0, 3)
      })
    },
    getUpcomingEvents: function () {

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#mainPageContainer {
  padding-top: 16%;
  min-height: 100vh;
  background-size: cover;
}

#bottomRow {
  padding-top: 10%
}

#cardSize {
  height: 500px;
}

#makeEventButton {
  margin-left: 15%;
  float: left;
  max-width:7%;
  max-height:7%;
}

#newEventText {
  margin-right: 20%;
  float: right;
  user-select: none;
}

</style>
