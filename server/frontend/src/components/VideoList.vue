<template>
  <a-list
    class="video-list"
    item-layout="horizontal"
    :data-source="data"
    :pagination="pagination"
  >
    <a-list-item slot="renderItem" slot-scope="item">
        <a-button type="danger" size="small" @click="deleteVideo(item.vid)">
          删除
        </a-button>
      <a-list-item-meta :description="item.brief">
        <a slot="title" :href="item.info"
          ><strong>{{ item.name }}</strong></a
        >
        <a-avatar slot="avatar" src="https://ibed.csgowiki.top/new_avatar" />
      </a-list-item-meta>
    </a-list-item>
  </a-list>
</template>
<script>
export default {
  props: {
    vlist: Array,
  },
  watch: {
    vlist: function (val) {
      this.data = val;
    },
  },
  data() {
    return {
      data: [],
      pagination: {
        onChange: (page) => {},
        pageSize: 8,
      },
    };
  },
  mounted() {
    this.data = this.vlist;
  },
  methods: {
    async deleteVideo(vid) {
      console.log(vid)
      vid = "%23" + vid.slice(1)
      const pwd = this.$cookies.get("ezm-server-pwd");
      this.$http
        .postData(`/op/delete?pwd=${pwd}&vid=${vid}`)
        .then((val) => {
          this.$message.success("删除成功", 3);
          console.log(val);
          // fetch new list
          this.$emit("refreshVList", "refresh");
        })
        .catch((err) => {
          this.$message.error(`删除失败：${err}`, 5);
        });
    },
  },
};
</script>
<style>
.video-list {
  min-height: 380px;
}
</style>
