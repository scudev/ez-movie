const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  css: {
    loaderOptions: {
      less: {
        javascriptEnabled: true,
        modifyVars: {
          '@primary-color': '#10aec2',
          '@link-color': '#10aec2'
        }
      }
    }
  }
})
