<template>
  <div id="event" :style="{'background-image': 'url(' + require('../../assets/pastEvent.jpg') + ')'}">
    <div>
      <b-container id="container">
        <b-row md="justify-content-md-center">
          <b-col >
            <p id="caption">{{this.date}}, ({{this.location}}) </p>
          </b-col>
      </b-row>
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
          >
            <template v-slot:cell(actions)="row">
              <div id="center">
                <p id="toggleBlock">{{getPlayerName(row, "0")}}</p>
                <ToggleButton
                  id="toggleBlock"
                  @change="onToggleButton($event, row.item.id)"
                  :value="getPlayerTeam(row.item.id)"
                  :labels="{checked: 'Team 1', unchecked: 'Team 0 '}"
                  :width=150
                />
                <p id="toggleBlock">{{getPlayerName(row, "1")}}</p>
              </div>
            </template>
          </b-table>
        </b-col>
      </b-row>
      <b-row md="justify-content-md-center">
        <b-col>
          <b-button pill block v-on:click="updateEvent">
            Update/Create event
          </b-button>
          <b-button pill block v-on:click="startEvent">
            Start event!
          </b-button>
        </b-col>
      </b-row>
    </b-container>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import ToggleButton from 'vue-js-toggle-button'

export default {
  name: 'Event',
  props: ['eventData', 'eventId'],
  component: {
    ToggleButton
  },
  data: function () {
    return {
      date: '',
      location: '',
      players: [],
      fields: [
        { key: 'actions', label: 'Team' }
      ]
    }
  },
  created: function () {
    this.setEventData(this.eventData)
  },
  methods: {
    setEventData: function (eventData) {
      this.date = this.eventData.date
      this.location = this.eventData.location
      this.players = this.eventData.players
      this.players.filter(player => player.team === null)
        .map(player => { player.team = '0' })
    },
    onToggleButton: function (event, playerId) {
      const team = event.value ? '1' : '0'
      this.players.filter(player => player.id === playerId)[0].team = team
    },
    getPlayerName (row, team) {
      if (this.players[row.index].team === team) {
        return this.players[row.index].player_name
      } else {
        return ''
      }
    },
    getPlayerTeam (playerId) {
      return this.players.filter(player => player.id === playerId)[0].team === '1'
    },
    updateEvent () {
      this.createEvent('C')
    },
    startEvent () {
      this.createEvent('P')
    },
    createEvent (status) {
      const data = {
        location: this.location,
        completed: status,
        date: new Date(this.date).toISOString(),
        event_player: this.players.map(
          player => {
            return {
              id: player.id,
              team: player.team,
              player: player.player_id
            }
          }
        )
      }
      console.log(JSON.stringify(data))
      axios.put('/v1/event/' + this.eventId + '/', data).then((response) => {
        this.$router.go()
      })
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
  padding: 5%
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

#toggleBlock {
  display: inline-block;
}

</style>
