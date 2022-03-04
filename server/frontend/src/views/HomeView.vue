<template>
  <div class="container">
    <div class="download-box">
      <a-input
        v-model="pwd"
        size="large"
        placeholder="请输入静态口令"
        @keydown.enter="queryVideoListByPwd"
      >
        <a-icon
          slot="addonAfter"
          :type="loading ? 'loading' : 'link'"
          class="icon"
          @click="queryVideoListByPwd"
        />
      </a-input>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pwd: "",
      loading: false,
    };
  },
  computed: {},
  watch: {},
  mounted() {},
  created() {},
  methods: {
    async queryVideoListByPwd() {
      this.$http.getData("/video/list", { pwd: this.pwd }).then((val) => {
        console.log(val);
      });
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
}
</style>
