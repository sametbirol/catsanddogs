/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'
import { createPinia } from 'pinia'

// Plugins
import { registerPlugins } from '@/plugins'
import router from '@/router'

const app = createApp(App)
			.use(createPinia())
			.use(router)

registerPlugins(app)

app.mount('#app')
