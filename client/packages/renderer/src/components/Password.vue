<template>
  <div>
    <el-input v-model="password" class="w-20 m-2" size="large" placeholder="输入静态口令">
      <template #prefix>
        <el-icon class="el-input__icon"><key /></el-icon>
      </template>
    </el-input>
    <div slot="footer">
      <el-button type="primary" @click="handelConfirm">确定</el-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { Key } from "@element-plus/icons-vue";
const password = ref("");
</script>

<style>
</style>