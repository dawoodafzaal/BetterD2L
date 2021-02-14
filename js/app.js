import Vue from 'vue'
import Router from 'vue-router'
import App from './App.vue'

import VueMaterial from 'vue-material'

Vue.config.devtools = true
Vue.use(Router)

Vue.use(VueMaterial)

import { routes } from './routes';

new Vue({
  router: new Router({
  	routes
  }),

  ...App
}).$mount('#app')