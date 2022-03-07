<template>
  <div class="container">
    <div class="show-box" v-if="!authed">
      <a-input
        v-model="pwd"
        size="large"
        placeholder="请输入静态口令"
        @keydown.enter="queryVideoListByPwd"
      >
        <a-icon
          slot="addonAfter"
          :type="'link'"
          class="icon"
          @click="queryVideoListByPwd"
        />
      </a-input>
    </div>
    <div class="show-box" v-else>
      authed
      <div class="logout-icon">
        <a-icon type="logout" class="icon" @click="logout()" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pwd: "",
      authed: false
    };
  },
  computed: {},
  watch: {},
  mounted() {
    this.pwd = this.$cookies.get('ezm-server-pwd')
    this.authed = (this.pwd != null)
  },
  created() {},
  methods: {
    async queryVideoListByPwd() {
      this.$cookies.remove('ezm-server-pwd')
      this.$cookies.set('ezm-server-pwd', this.pwd)
      this.authed = true
      this.$http.getData("/v/list", { pwd: this.pwd }).then((val) => {
        console.log(val);
      });
    },
    logout() {
      this.$cookies.remove('ezm-server-pwd')
      this.authed = false
    }
  },
};
</script>

<style scoped lang="less">
.container {
  box-sizing: border-box;
  padding: 32px;
  position: relative;
  height: calc(100% - 28px);
  .show-box {
    padding: 80px 80px;
    /deep/ .ant-input-group-addon {
      background: @primary-color;
      border: none;
    }
    .icon {
      color: #ffffff;
      font-size: 18px;
    }
  }
  .logout-icon{
    position: absolute;
    bottom: 180px;
    right: 64px;
    z-index: 99;
    cursor: pointer;
    .icon{
      font-size: 28px;
      color: @primary-color;
    }
  }
}
</style>
