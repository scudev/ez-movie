<template>
  <a-list
    class="video-list"
    item-layout="horizontal"
    :data-source="data"
    :pagination="pagination"
  >
    <a-list-item slot="renderItem" slot-scope="item">
      <a slot="actions">edit</a>
      <a slot="actions">more</a>
      <a-list-item-meta :description="item.brief">
        <a slot="title" :href="item.info"><strong>{{ item.name }}</strong></a>
        <a-avatar
          slot="avatar"
          src="https://ibed.csgowiki.top/new_avatar"
        />
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
  methods: {},
};
</script>
<style>
.video-list {
  min-height: 380px;
}
</style>
