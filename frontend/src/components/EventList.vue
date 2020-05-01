<template>
  <div id="eventList" :style="{'background-image': 'url(' + require('../assets/eventList.jpg') + ')'}">
    <b-container fluid>
      <b-row class="justify-content-md-center">
        <b-col md="auto">
          <b-table
            hover
            table-variant="light"
            head-variant="light"
            :items="upcomingEvents"
            :fields="fields"
            no-border-collapse
            bordered
          >
            <template v-slot:cell(actions)="row">
              <b-button size="sm" @click="redirectToEventDetails(row.item.id)" class="mr-1">
                Details
              </b-button>
            </template>
          </b-table>
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center">
        <b-col md="auto">
          <b-table
            hover
            table-variant="light"
            head-variant="light"
            :items="pendingEvents"
            :fields="fields"
            no-border-collapse
            bordered
          >
            <template v-slot:cell(actions)="row">
              <b-button size="sm" @click="redirectToEventDetails(row.item.id)" class="mr-1">
                Details
              </b-button>
            </template>
          </b-table>
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center">
        <b-col md="auto">
          <b-table
            hover
            table-variant="light"
            head-variant="light"
            :items="finishedEvents"
            :fields="fields"
            no-border-collapse
            bordered
          >
            <template v-slot:cell(actions)="row">
              <b-button size="sm" @click="redirectToEventDetails(row.item.id)" class="mr-1">
                Details
              </b-button>
            </template>
          </b-table>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'EventList',
  data: function () {
    return {
      upcomingEvents: [],
      finishedEvents: [],
      pendingEvents: [],
      fields: [
        { key: 'date', label: 'Date', class: 'text-center' },
        { key: 'location', label: 'Location', class: 'text-center' },
        { key: 'score_a', label: 'Score A', class: 'text-center' },
        { key: 'score_b', label: 'Score B', class: 'text-center' },
        { key: 'actions', label: 'Actions' }
      ]
    }
  },
  created: function () {
    this.fetchEvents()
  },
  methods: {
    fetchEvents () {
      return axios.get('v1/event')
        .then(response => {
          const events = response.data
          this.finishedEvents = events.filter(event => event.completed === 'F')
          this.pendingEvents = events.filter(event => event.completed === 'P')
          this.upcomingEvents = events.filter(event => event.completed === 'C')
        })
    },
    redirectToEventDetails (data) {
      this.$router.push({ name: 'event', params: { id: data } })
    }
  }
}
</script>

<style scoped>

#eventList {
  padding-top: 16%;
  min-height: 100vh;
  background-size: cover;
}

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
