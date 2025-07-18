import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'

export default defineNuxtConfig({
  compatibilityDate: '2025-05-15',

  // モジュールに Vuetify Vite プラグインを追加
  modules: [
    "@nuxt/image",
    "@uploadthing/nuxt",
    "@nuxtjs/tailwindcss",

    // Vuetify を Vite 経由で追加
    (_options, nuxt) => {
      nuxt.hooks.hook('vite:extendConfig', (config) => {
        // @ts-expect-error: config.plugins に push 可能
        config.plugins.push(vuetify({ autoImport: true }))
      })
    },
  ],

  // Vuetify 用に必要な Vite 設定
  vite: {
    vue: {
      template: {
        transformAssetUrls,
      },
    },
  },

  // Vuetify のためのビルド設定
  build: {
    transpile: ['vuetify'],
  },
})
