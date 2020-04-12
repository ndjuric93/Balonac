import Router from 'vue-router'
import MainPage from '../components/MainPage.vue'
import Event from '../components/Event.vue'
import EventList from '../components/EventList.vue'
import EventCreator from '../components/EventCreator.vue'
import PlayerList from '../components/PlayerList.vue'
import Login from '../components/Login'
import Logout from '../components/Logout'

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'main_page',
      component: MainPage
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/logout',
      name: 'logout',
      component: Logout
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
    },
    {
      path: '/events/:id',
      name: 'event',
      component: Event,
      props: true
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/login']
  const authRequired = !publicPages.includes(to.path)
  const loggedIn = !!localStorage.getItem('token')

  if (authRequired && !loggedIn) {
    return next('/login')
  }
  next()
})

export default router
