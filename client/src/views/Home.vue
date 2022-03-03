<template>
  <div class="container">
    <div class="download-logo fr ac jc">
      <img src="../assets/images/logo.png" alt="">
    </div>
    <div class="download-box">
      <a-input v-model="url" size="large" placeholder="请输入视频地址" @keydown.enter="download">
        <a-icon slot="addonAfter" :type="loading ? 'loading' : 'arrow-down'" class="icon" @click="download" />
      </a-input>
    </div>
    <div class="setting" v-if="$route.path === '/'">
      <a-icon type="setting" class="icon" @click="openSettingDrawer()" />
    </div>
    <div class="user" v-if="$route.path === '/'">
      <a-icon type="user" class="icon" @click="$refs.userModal.show()"/>
    </div>
  </div>
</template>

<script>
import base from '../mixin/base'
export default {
  mixins: [base],
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
  .setting{
    position: absolute;
    left: 16px;
    bottom: 16px;
    z-index: 100;
    color: @primary-color;
    font-size: 16px;
  }
  .user{
    position: absolute;
    right: 16px;
    bottom: 16px;
    z-index: 100;
    color: @primary-color;
    font-size: 16px;
  }
}
</style>
