module.exports = {
    pluginOptions: {
      electronBuilder: {
        nodeModulesPath: ['../../node_modules', './node_modules'],
        nodeIntegration: true,
        contextIsolation: false,
        builderOptions: {
          productName: 'ez-movie-client',
          appId: 'com.example.ez-movie-client',
          dmg: {
            contents: [
              {
                x: 410,
                y: 150,
                type: 'link',
                path: '/Applications'
              },
              {
                x: 130,
                y: 150,
                type: 'file'
              }
            ],
            sign: false,
            icon: 'build/icons/icon.ico'
          },
          mac: {
            icon: 'build/icons/icon.icns',
            identity: null,
            target: {
              target: 'dmg',
              arch: ['x64', 'arm64', 'universal']
            }
          },
          nsis: {
            oneClick: false,
            perMachine: false,
            allowToChangeInstallationDirectory: true,
            installerIcon: 'build/icons/icon.ico',
            uninstallerIcon: 'build/icons/icon.ico',
            installerHeaderIcon: 'build/icons/icon.ico',
            createDesktopShortcut: true
          },
          win: {
            icon: 'build/icons/icon.ico',
            target: 'nsis'
          },
          linux: {
            icon: 'build/icons'
          }
        }
      }
    },
    css: {
      loaderOptions: {
        less: {
          javascriptEnabled: true,
          modifyVars: {
            // less 全局变量
            // 主色
            '@primary-color': '#e2c027',
            '@link-color': '#e2c027'
          }
        }
      }
    }
  }
  