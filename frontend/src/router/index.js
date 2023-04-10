import { createRouter, createWebHistory } from "vue-router";
// import ViewMainPage from '@/views/ViewMainPage.vue'
import ViewAuth from '@/views/ViewAuth.vue'
// import ViewProfile from '@/views/ViewProfile.vue'
import { useStoreBasic } from '@/stores/storeBasic.js'
import { useStoreImage } from "@/stores/storeImages";
let storeBasic
let storeImage
const routes = [
	{
		path: '/auth',
		name: 'auth',
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
	const storeBasic = useStoreBasic()
	const storeImage = useStoreImage()
	
	try{
		storeBasic.get_current_user_by_token()
	}
	catch(err) {
		storeBasic.logout()
	}
	try {
		if (storeBasic.user && to.name === 'auth') {
			storeImage.init()
			return { name: 'posts' }
		}
		if (!storeBasic.user && to.name !== 'auth') {
			return false
		}
		if (storeImage.posts == null && storeBasic.user) {
			storeImage.init()
		}
	}
	catch(err) {
		console.log(err)
	}
})

export default router