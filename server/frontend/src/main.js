import Vue from 'vue'
import antd from 'ant-design-vue'
import VueCookies from 'vue-cookies'
import App from './App.vue'
import router from './router'
import api from './utils/api'
import 'ant-design-vue/dist/antd.less'
import './assets/style/main.less'

Vue.use(antd)
Vue.use(VueCookies)

Vue.prototype.$http = api
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
