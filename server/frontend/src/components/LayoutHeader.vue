<template>
  <div class="header fr ac jc">
    {{projectName}}
    <div class="route-icon">
      <a-icon :type="iconData.icon" class="icon" @click="goRoute(iconData.route)" />
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      projectName: "爱看电影 服务端",
      iconDataMap: {
        '/': {
          icon: 'unordered-list',
          route: '/explore'
        },
        '/explore': {
          icon: 'rollback',
          route: '/'
        }
      },
      iconData: {
        icon: 'download',
        route: '/explore'
      }
    }
  },
  components: {},
  computed: {},
  watch: {
    '$route.path': {
      handler (val) {
        this.iconData = this.iconDataMap[val]
      },
      immediate: true
    }
  },
  mounted () {},
  created () {},
  methods: {
    goRoute (route) {
      this.$router.push(route)
    }
  }
}
</script>

<style scoped lang="less">
.header{
  position: relative;
  box-sizing: border-box;
  height: 28px;
  -webkit-app-region: drag;
  color: @primary-color;
  font-weight: bold;
  font-size: 32px;
  .route-icon{
    position: absolute;
    bottom: -53px;
    left: 64px;
    z-index: 99;
    cursor: pointer;
    .icon{
      font-size: 28px;
      color: @primary-color;
    }
  }
}
</style>
