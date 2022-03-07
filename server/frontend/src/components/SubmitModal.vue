<template>
  <div>
    <a-modal
      v-model="visible"
      title="提交表单"
      @ok="doSubmit"
      @cancel="doCancel"
      ok-text="提交"
      cancel-text="取消"
      :confirm-loading="confirmLoading"
    >
      <a-form
        :form="form"
        :label-col="{ span: 5 }"
        :wrapper-col="{ span: 16 }"
        @submit="doSubmit"
      >
        <a-form-item label="视频名称">
          <a-input
            v-decorator="[
              'name',
              {
                rules: [{ required: true, message: '请不要留空' }],
              },
            ]"
          />
        </a-form-item>
        <a-form-item label="视频简介">
          <a-input
            v-decorator="[
              'brief',
              {
                rules: [{ required: true, message: '请不要留空' }],
              },
            ]"
          />
        </a-form-item>
        <a-form-item label="片源类型">
          <a-select
            v-decorator="[
              'tag',
              {
                rules: [{ required: true, message: '请选择视频源的类型' }],
              },
            ]"
            placeholder="请选择视频源的类型"
            @change="handleSelectChange"
          >
            <a-select-option
              v-for="tag in this.videoTags"
              :key="tag.index"
              :value="tag.index"
            >
              {{ tag.label }}
            </a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="视频简介">
          <a-textarea
            placeholder="请输入片源：在线链接 或 磁力链接"
            :auto-size="{ minRows: 2, maxRows: 6 }"
            v-decorator="[
              'info',
              {
                rules: [{ required: true, message: '请输入片源' }],
              },
            ]"
          />
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>
<script>
export default {
  data() {
    return {
      visible: false,
      confirmLoading: false,
      formLayout: "horizontal",
      form: this.$form.createForm(this, { name: "coordinated" }),
      videoTags: [
        { index: 0, label: "在线免认证片源" },
        { index: 1, label: "在线需认证片源" },
        { index: 2, label: "离线片源" },
      ],
    };
  },
  methods: {
    show() {
      this.visible = true;
    },
    handleSelectChange(value) {
      this.form.setFieldsValue({
        // note: `Hi, ${value === 'male' ? 'man' : 'lady'}!`,
      });
    },
    doSubmit(e) {
      this.form.validateFields((err, values) => {
        if (!err) {
          this.confirmLoading = true;
          const pwd = this.$cookies.get("ezm-server-pwd");
          this.$http
            .postData(`/op/add_new?pwd=${pwd}`, values)
            .then((val) => {
              this.$message.success("数据提交成功", 5);
              this.confirmLoading = false;
              this.visible = false;
              // fetch new list
              this.$emit('refreshVList', 'refresh')
            })
            .catch((err) => {
              this.$message.error(`数据提交失败：${err}`, 5);
              this.confirmLoading = false;
              this.visible = true;
            });
        }
      });
    },
    doCancel(e) {},
  },
};
</script>
