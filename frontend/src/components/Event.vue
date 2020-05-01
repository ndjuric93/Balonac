<template>
  <PastEvent
    v-if="this.eventData.completed==='F'"
    :eventData=this.eventData
    :eventId=this.id
  />
  <UpcomingEvent
    v-else-if="this.eventData.completed==='C'"
    :eventData=this.eventData
    :eventId=this.id
  />
  <PastEvent
    v-else-if="this.eventData.completed==='P'"
    :eventData=this.eventData
    :eventId=this.id
  />
</template>

<script>
import axios from 'axios'
import PastEvent from './helper/PastEvent'
import UpcomingEvent from './helper/UpcomingEvent'

export default {
  name: 'Event',
  components: {
    PastEvent,
    UpcomingEvent
  },
  props: ['id'],
  data: function () {
    return {
      eventData: {}
    }
  },
  created: function () {
    return axios.get('v1/event/' + this.id)
      .then(response => {
        this.eventData = response.data
      })
  }
}
</script>
