# ez-movie

## Introduction

当你不在父母身边，而父母想看电影时，他们只需要：

1. 向你说明想要看的电影/视频
2. 将家里的电脑开机
3. 点击桌面上由本项目提供的某个应用

点击后，该应用会根据你服务端预设的片源作出一系列自动化行为：
- 【在线片源】自动打开浏览器并跳转至指定在线片源播放
- 【离线片源】自动下载视频文件，下载完成后提示并调用视频播放器播放


## Building

### ez-movie-client

使用[**electron-vue-vite**](https://github.com/caoxiemeihao/electron-vue-vite)框架，推荐使用yarn构建

```bash

cd client/

# 设置electron镜像，否则容易构建失败
yarn config set ELECTRON_MIRROR https://npm.taobao.org/mirrors/electron/

# 安装依赖
yarn

yarn dev
```

### ez-movie-server
TODO