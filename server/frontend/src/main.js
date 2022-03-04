import Vue from 'vue'
import App from './App.vue'
import router from './router'
import antd from 'ant-design-vue'
import api from './utils/api'
import 'ant-design-vue/dist/antd.less'
import './assets/style/main.less'

Vue.use(antd)

Vue.prototype.$http = api
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
