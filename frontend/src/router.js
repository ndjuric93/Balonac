import Vue from 'vue'
import Router from 'vue-router'
import MainPage from './components/MainPage.vue'
import EventList from './components/EventList.vue'
import EventCreator from './components/EventCreator.vue'
import PlayerList from './components/PlayerList.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'main_page',
      component: MainPage
    },
    {
      path: '/events',
      name: 'events',
      component: EventList
    },
    {
      path: '/players',
      name: 'players',
      component: PlayerList
    },
    {
      path: '/events/create',
      name: 'eventCreator',
      component: EventCreator
    }
  ]
})
