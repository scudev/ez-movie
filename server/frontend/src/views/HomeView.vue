<template>
  <div class="container">
    <div class="download-box">
      <a-input v-model="url" size="large" placeholder="请输入静态口令" @keydown.enter="download">
        <a-icon slot="addonAfter" :type="loading ? 'loading' : 'link'" class="icon" @click="download" />
      </a-input>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      url: '',
      loading: false
    }
  },
  computed: {},
  watch: {},
  mounted () {},
  created () {},
  methods: {
    async download () {
    }
  }
}
</script>

<style scoped lang="less">
.container{
  box-sizing: border-box;
  padding: 16px;
  position: relative;
  height: calc(100% - 28px);
  .download-logo{
    margin: 30px 0px 40px 0px;
    img{
      transform: scale(.6);
    }
  }
  .download-box{
    padding: 0px 64px;
    /deep/ .ant-input-group-addon{
      background: @primary-color;
      border: none;
    }
    .icon{
      color: #ffffff;
      font-size: 18px;
    }
  }
}
</style>
