import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'


export const useStoreBasic = defineStore('storeBasic', {

	state: () => {
		return {
			side: "Animal",
			user: null,
			router: useRouter()
		}
	},

	getters: {

	},

	actions: {
		async init() {
			await axios.get('/auth/')
				.then((res) => {
					this.user = res.data.user
					if (res.data == false) {
						this.router.push("/auth")
					}
					this.router.push("/mainpage")
				})
				.catch((error) => {
					console.error(error);
				});
		},
		async get_current_user_by_token() {
			await axios.get('/auth/')
				.then((res) => {
					this.user = res.data.user
					if (res.data == false) {
						this.router.push("/auth")
					}
				})
				.catch((error) => {
					console.error(error);
				});
		},
		createUser(data) {
			data.side = this.side
			axios.post('auth/register', data, {
				headers: {
					'Content-Type': 'application/json'
				}
			})
				.then((res) => {
					let loginform = { "username": res.data.username, "password": res.data.password }
					this.loginUser(loginform)
				})
		},
		async loginUser(data) {
			await axios.post('auth/login', data, {
				headers: {
					'Content-Type': 'application/json'
				}
			}).then(res => {
				this.init()
			}
			)
		},
		async logout() {
			await axios.get('/auth/logout')
				.then((res) => {
					this.router.push("/auth")
				})
				.catch((error) => {
					console.error(error);
				});
		}

	}
})