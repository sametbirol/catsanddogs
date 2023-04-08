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
		},
		checkPassword(password) {

			const password_length = password.length
			const format = /[ !@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/
				  
			let contains_eight_characters = false

			if (password_length > 8) {
				contains_eight_characters = true
			} 
			else {
				contains_eight_characters = false
				  }
				  
			const contains_number = /\d/.test(password)
			const contains_uppercase = /[A-Z]/.test(password)
			const contains_special_character = format.test(password)
			
			if (contains_eight_characters === true &&
						  contains_special_character === true &&
						  contains_uppercase === true &&
						  contains_number === true) {
							  return true			
			} 
			else {
			  return false
			}
		  }
		}
	  }
)