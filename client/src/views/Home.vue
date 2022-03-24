<template>
  <div class="container">
    <div class="home-logo fr ac jc">
      <img src="../assets/images/logo.png" alt="" />
    </div>
    <div class="home-box">
      <a-input
        v-model="pwd"
        size="large"
        placeholder="请输入静态口令"
        @keydown.enter="submitPwd"
      >
        <a-icon
          slot="addonAfter"
          :type="loading ? 'loading' : 'link'"
          class="icon"
          @click="submitPwd"
        />
      </a-input>
    </div>
    <div class="setting" v-if="$route.path === '/'">
      <a-icon type="setting" class="icon" @click="openSettingDrawer()" />
    </div>
  </div>
</template>

<script>
import base from "../mixin/base";

export default {
  mixins: [base],
  data() {
    return {
      url: "",
      loading: false,
      vlist: [],
      authed: false,
      pwd: "",
    };
  },
  computed: {},
  watch: {},
  mounted() {
    this.pwd = window.ipcRenderer.sendSync("get-store", "ezm-client-pwd");
    this.authed = window.ipcRenderer.sendSync("get-store", "ezm-client-authed");
    if (this.authed) {
      this.$router.push("/video-list");
    }
  },
  created() {},
  methods: {
    openSettingDrawer() {},
    submitPwd() {
      this.authed = true;
      window.ipcRenderer.send("set-store", ["ezm-client-pwd", this.pwd]);
      window.ipcRenderer.send("set-store", ["ezm-client-authed", this.authed]);
      this.$router.push("/video-list");
    },
  },
};
</script>

<style scoped lang="less">
.container {
  box-sizing: border-box;
  padding: 16px;
  position: relative;
  height: calc(100% - 28px);
  .home-logo {
    margin: 30px 0px 40px 0px;
    img {
      transform: scale(0.6);
    }
  }
  .home-box {
    padding: 0px 64px;
    /deep/ .ant-input-group-addon {
      background: @primary-color;
      border: none;
    }
    .icon {
      color: #ffffff;
      font-size: 18px;
    }
  }
  .setting {
    position: absolute;
    left: 16px;
    bottom: 16px;
    z-index: 100;
    color: @primary-color;
    font-size: 16px;
  }
}
</style>
