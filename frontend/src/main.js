/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'

// Composables
import { createApp,markRaw } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios';

// Plugins
import { registerPlugins } from '@/plugins'
import router from '@/router'
createPinia().use(({ store }) => {
	store.router = markRaw(router)
	})
const app = createApp(App)
			.use(createPinia())
			

axios.defaults.withCredentials = true
axios.defaults.baseURL = "http://localhost:8000/"

app.use(router)
registerPlugins(app)

app.mount('#app')
