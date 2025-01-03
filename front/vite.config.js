import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

export default defineConfig({
  plugins: [svelte()],
  build: {
    outDir: '../static', // Сохраняем build в backend/static
    emptyOutDir: true,           // Очищаем папку перед сборкой
  },
  base: '/static/',
  server: {
    port: 5173,                  // Порт для dev-сервера (можно изменить)
  },
})