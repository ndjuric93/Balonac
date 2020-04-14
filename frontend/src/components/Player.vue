<template>
    <div>
<div class="Player">
    <h1>{{playerDetails.name}}</h1>
</div>
    </div>
</template>

<script>
import axios from 'axios'

axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

export default {
  name: 'Player',
  props: {
    id: Number
  },
  data: function () {
    return {
      playerDetails: {
        player: []
      }
    }
  },
  mounted: function () {
    return axios.get(process.env.VUE_APP_BASE_URL + 'api/v1/player/' + this.id)
      .then(response => {
        this.playerDetails = response.data
      }
      )
  }
}
</script>

<style scoped>

</style>
