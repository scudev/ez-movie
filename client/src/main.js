import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import antd from 'ant-design-vue'
import checkUpdate from './components/CheckUpdate/index'
import 'ant-design-vue/dist/antd.less'
import './assets/style/main.less'

Vue.use(antd)
Vue.use(checkUpdate)

const { ipcRenderer } = require('electron')
window.ipcRenderer = ipcRenderer

Vue.config.productionTip = false
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
