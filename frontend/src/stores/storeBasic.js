import { defineStore } from 'pinia'
import axios from 'axios'

export const useStoreBasic = defineStore( 'storeBasic', {

	state: () => {
		return {
			side: "Animal",
			msg: Array,
			msgg: Array
		}
	},
	
	getters:{

	},

	actions:{
		getMessage() {
			axios.get('auth')
			  .then((res) => {
				this.msg = res.data;
			  })
			  .catch((error) => {
				console.error(error);
			  });

	},
		createUser(data){
			axios.post('auth', data,{
				headers: {
					'Content-Type': 'application/json'
				}
			})
			.then(res => console.log(res))
		}
}
})