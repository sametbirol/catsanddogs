import { createRouter, createWebHashHistory } from "vue-router";
import ViewMainPage from '@/views/ViewMainPage.vue'
import ViewBos from '@/views/ViewBos.vue'

const routes = [
	{
		path: '/',
		name: 'bos',
		component: ViewBos
	},
	{
		path: '/mainpage',
		name: 'posts',
		component: ViewMainPage
	}
]

const router = createRouter({
	history: createWebHashHistory(),
	routes: routes
})

export default router