<template>
  <div>
    <a-modal v-model="visible" title="提交表单" @ok="doSubmit">
      
    </a-modal>
  </div>
</template>
<script>
export default {
  data() {
    return {
      visible: false,
    };
  },
  methods: {
    show() {
      this.visible = true;
    },
    doSubmit(e) {
      this.visible = false;
    },
  },
};
</script>
