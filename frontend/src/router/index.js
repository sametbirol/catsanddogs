import { createRouter, createWebHistory } from "vue-router";
// import ViewMainPage from '@/views/ViewMainPage.vue'
import ViewAuth from '@/views/ViewAuth.vue'
// import ViewProfile from '@/views/ViewProfile.vue'
import { useStoreBasic } from '@/stores/storeBasic.js'
let store
const routes = [
	{
		path: '/auth',
		name: 'Auth',
		component: ViewAuth
	},
	{
		path: '/mainpage',
		name: 'posts',
		component: () => import(
			/* webpackPrefetch: false */
			/* webpackPreload: false */
			'@/views/ViewMainPage.vue'
		)
	},
	{
		path: '/profile',
		name: 'profile',
		component: () => import(
			/* webpackPrefetch: false */
			/* webpackPreload: false */
			'@/views/ViewProfile.vue'
		)
	}
]

const router = createRouter({
	history: createWebHistory(),
	routes: routes
})

router.beforeEach(async (to, from) => {
	const store = useStoreBasic()
	
	store.get_current_user_by_token()
	try {
		if (store.user && to.name === 'Auth') {
			return { name: 'posts' }
		}
		if (!store.user && to.name !== 'Auth') {
			return false
		}
	}
	catch(err) {
		console.log(err)
	}
})

export default router