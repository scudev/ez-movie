<template>
  <div class="header fr ac jc">
    <div class="icons">
      <a-icon class="icon icon1" @click="close" type="close" />
      <a-icon class="icon icon2 ml8" @click="min" type="minus" />
    </div>
    <div class="route-icon">
      <a-icon
        :type="iconData.icon"
        class="icon"
        @click="goRoute(iconData.route)"
      />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      iconDataMap: {
        "/": {
          icon: "unordered-list",
          route: "/video-list",
        },
        "/video-list": {
          icon: "rollback",
          route: "/",
        },
      },
      iconData: {
        icon: "unordered-list",
        route: "/video-list",
      },
    };
  },
  components: {},
  computed: {},
  watch: {
    "$route.path": {
      handler(val) {
        this.iconData = this.iconDataMap[val];
      },
      immediate: true,
    },
  },
  mounted() {},
  created() {},
  methods: {
    close() {
      window.ipcRenderer.send("open-close-dialog", "hello");
    },
    min() {
      window.ipcRenderer.send("minimize-window", "hello");
    },
    goRoute(route) {
      if (route === "/") {
        window.ipcRenderer.send("set-store", ["ezm-client-authed", false]);
        this.$router.push(route);
      } else if (route === "/video-list") {
        const pwd = window.ipcRenderer.sendSync("get-store", "ezm-client-pwd");
        if (pwd == null) {
          this.$message.warning("请先输入静态口令");
        } else {
          window.ipcRenderer.send("set-store", ["ezm-client-authed", true]);
          this.$router.push(route);
        }
      }
    },
  },
};
</script>

<style scoped lang="less">
.header {
  position: relative;
  box-sizing: border-box;
  height: 28px;
  -webkit-app-region: drag;
  color: #99ccff;
  font-weight: bold;
  .icons {
    position: absolute;
    top: 50%;
    left: 8px;
    transform: translateY(-50%);
    z-index: 1000;
    -webkit-app-region: no-drag;
    .icon {
      border-radius: 50%;
      font-size: 10px;
      font-weight: bold;
      padding: 2px;
      &.icon1 {
        background: rgb(223, 96, 88);
        color: rgb(223, 96, 88);
      }
      &.icon2 {
        background: rgb(237, 186, 63);
        color: rgb(237, 186, 63);
      }
      &:hover {
        &.icon1 {
          color: rgb(27, 27, 27);
        }
        &.icon2 {
          color: rgb(27, 27, 27);
        }
      }
    }
  }
  .route-icon {
    position: absolute;
    bottom: -53px;
    right: 16px;
    z-index: 99;
    cursor: pointer;
    .icon {
      font-size: 36px;
      color: #ffffcc;
    }
  }
}
</style>
