<template>
<div
  :style="{'background-image': 'url(' + require('../assets/login.jpg') + ')'}"
  id="container"
>
  <b-container fluid="sm" >
    <b-row align-v="center" align-h="center">
      <b-col md="6">
        <div id="wrapper">
          <div id="h">
            <p id="preHeaderText">Welcome to</p>
            <h1 id="headerText">BALLOON</h1>
              <b-form-input
                class="inputLarge"
                size="lg"
                placeholder="Username"
                v-model="username"
              >
              </b-form-input>
              <b-form-input
                class="inputLarge"
                size="lg"
                type="password"
                placeholder="Password"
                v-model="password"
              >
              </b-form-input>
              <div id="submitButton">
                <b-button type="submit" variant="primary" @click="login">Login</b-button>
              </div>
          </div>
        </div>
      </b-col>
    </b-row>
  </b-container>
</div>
</template>

<script>
import router from '../services/router'

export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login () {
      this.$store.dispatch('LOGIN', {
        username: this.username,
        password: this.password
      })
        .then(success => {
          router.push({ name: 'main_page' })
        })
    }
  }
}
</script>

<style scoped>

#container {
  padding-top: 15%;
  min-height: 100vh;
  background-size: cover;
}

#h {
  width: auto;
  height: auto;
  border-radius: 20px;
  backdrop-filter: blur(3px);
  padding: 20px;
}

#preHeaderText {
  font: Proxima;
  font-size: 20px;
  color: azure
}

#headerText {
  font: Proxima;
  font-size: 40px;
  color: azure
}

#inputLarge {
  height: 100%;
  padding-left: 10%;
}

#wrapper {
  margin: 0;
  padding: 0px 10px;
  width: 100%;
}
</style>
