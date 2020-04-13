import axios from 'axios'

function getPlayers () {
  return axios.get(process.env.VUE_APP_BASE_URL + 'api/v1/player')
    .then(response => { return response.data })
}

export default getPlayers
