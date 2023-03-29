import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router'

export const useStoreBasic = defineStore('storeBasic', {

	state: () => {
		return {
			side: "Animal",
			msg: Array,
			msgg: "",
			user: null,
		}
	},

	getters: {

	},

	actions: {
		authenticate_user() {
			axios.get('auth')
				.then((res) => {
					// this.msg = res.data;
					this.msg = res.data.user
					if (this.msg) {
						return true
					}
				})
				.then((res) => {
					if (res) {
						router.push("/mainpage")
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
				.then(res => console.log(res))//returns "user succesfully created" if succesful
		},
		loginUser(data) {
			axios.post('auth/login', data, {
				headers: {
					'Content-Type': 'application/json'
				}
			})
				.then(res => console.log(res))//returns token
		},
		logout(){
			axios.get('auth/logout')
			.then((res) => {
				console.log(res)
			})
			.catch((error) => {
				console.error(error);
			});
		}

	}
})