import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/HomeView.vue')
  },
  {
    path: '/explore',
    name: 'Explore',
    component: () => import('../views/ExploreView.vue')
  }
]

const router = new VueRouter({
  routes,
  mode: 'history',
  base: '/'
})

export default router
