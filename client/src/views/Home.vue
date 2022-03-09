<template>
  <div class="container">
    <div class="download-logo fr ac jc">
      <img src="../assets/images/logo.png" alt="" />
    </div>
    <div class="download-box">
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
    this.authed = this.pwd != null;
    if (this.authed) {
      this.submitPwd();
    }
  },
  created() {},
  methods: {
    async submitPwd() {
      this.loading = true;
      this.$http
        .getData("/v/list", { pwd: this.pwd })
        .then((val) => {
          this.vlist = val;
          this.loading = false;
          this.authed = true;
          window.ipcRenderer.send("set-store", ["ezm-client-pwd", this.pwd]);
          if (this.vlist.length > 0) {
            window.ipcRenderer.send("open-external", this.vlist[0]["info"]);
          }
          this.$message.success("请求成功", 5);
        })
        .catch((err) => {
          this.authed = false;
          this.loading = false;
          window.ipcRenderer.send("delete-store", ["ezm-client-pwd", this.pwd]);
          this.$message.error(`请求错误: ${err}`, 5);
        });
    },
    openSettingDrawer() {},
  },
};
</script>

<style scoped lang="less">
.container {
  box-sizing: border-box;
  padding: 16px;
  position: relative;
  height: calc(100% - 28px);
  .download-logo {
    margin: 30px 0px 40px 0px;
    img {
      transform: scale(0.6);
    }
  }
  .download-box {
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
