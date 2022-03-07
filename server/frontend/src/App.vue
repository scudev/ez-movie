<template>
  <div id="app">
    <layout-header />
    <router-view></router-view>
  </div>
</template>

<script>
import LayoutHeader from './components/LayoutHeader'
export default {
  components: { LayoutHeader },
  mounted() {}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
