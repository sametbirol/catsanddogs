import { createRouter, createWebHistory } from "vue-router";
import ViewMainPage from '@/views/ViewMainPage.vue'
import ViewAuth from '@/views/ViewAuth.vue'
import ViewProfile from '@/views/ViewProfile.vue'

const routes = [
	{
		path: '/',
		name: 'Auth',
		component: ViewAuth
	},
	{
		path: '/mainpage',
		name: 'posts',
		component: ViewMainPage
	},
	{
		path: '/profile',
		name: 'profile',
		component: ViewProfile
	}
]

const router = createRouter({
	history: createWebHistory(),
	routes: routes
})

export default router