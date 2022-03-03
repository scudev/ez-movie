import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router'
import antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.less'
import './assets/style/main.less'

Vue.use(antd)

Vue.prototype.$axios = axios
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
