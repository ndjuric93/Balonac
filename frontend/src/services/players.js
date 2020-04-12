import axios from 'axios'

function getPlayers () {
  return axios.get('v1/player')
    .then(response => {
      return response.data
    })
}

export default getPlayers
