<template>
  <div class="container">
    <a-list
      class="video-list"
      item-layout="horizontal"
      :data-source="data"
      :loading="loading"
      :pagination="pagination"
      size="large"
    >
      <a-list-item
        slot="renderItem"
        slot-scope="item"
        @click="openWebpage(item.info)"
        @mouseover="changeActive($event)"
        @mouseleave="removeActive($event)"
      >
        <a-list-item-meta :description="item.brief">
          <a slot="title" class="video-item"
            ><strong>{{ item.name }}</strong></a
          >
          <a-avatar slot="avatar" src="https://ibed.csgowiki.top/new_avatar" />
        </a-list-item-meta>
      </a-list-item>
    </a-list>
  </div>
</template>
<script>
export default {
  watch: {},
  data() {
    return {
      data: [],
      pagination: {
        onChange: (page) => {},
        pageSize: 5,
      },
      loading: false,
      pwd: "",
      authed: false,
    };
  },
  mounted() {
    this.pwd = window.ipcRenderer.sendSync("get-store", "ezm-client-pwd");
    this.authed = window.ipcRenderer.sendSync("get-store", "ezm-client-authed");
    if (!this.authed) {
      this.$router.push("/");
    }
    this.getvListByPwd();
  },
  methods: {
    async getvListByPwd() {
      this.loading = true;
      this.$http
        .getData("/v/list", { pwd: this.pwd })
        .then((val) => {
          this.data = val;
          this.loading = false;
          // this.$message.success("请求成功", 2);
        })
        .catch((err) => {
          this.loading = false;
          this.$message.error(`请求错误: ${err}`, 3);
        });
    },
    openWebpage(url) {
      window.ipcRenderer.send("open-external", url);
    },
    changeActive($event) {
      $event.currentTarget.className = "active";
    },
    removeActive($event) {
      $event.currentTarget.className = "";
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
  .active {
    cursor: pointer;
  }
  .video-list {
    margin-top: 60px;
    margin-left: 100px;
    margin-right: 100px;
    margin-bottom: 60px;
  }
  .video-item {
    color: #ffffcc;
  }
}
</style>
