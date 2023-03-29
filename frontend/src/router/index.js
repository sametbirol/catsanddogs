import { createRouter, createWebHistory } from "vue-router";
import ViewMainPage from '@/views/ViewMainPage.vue'
import ViewAuth from '@/views/ViewAuth.vue'
import ViewProfile from '@/views/ViewProfile.vue'
import { useStoreBasic } from '@/stores/storeBasic.js'
let store
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

router.beforeEach(async (to, from) => {
	const store = useStoreBasic()
	try {
		if (store.user.id && to.name === 'Auth') {
			return { name: 'posts' }
		}
		if (!store.user.id && to.name !== 'Auth') {
			return false
		}
		if (from.name !== 'Auth' && to.name === 'Auth') {
			store.logout()
			return { name: 'Auth' }
		}
	}
	catch(err) {
		console.log(err)
	}
})

export default router