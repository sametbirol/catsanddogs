import { defineStore } from 'pinia'
import { storage } from '@/firebasejs/firebase'
import { ref as storageRef, uploadBytes, deleteObject ,getDownloadURL} from "firebase/storage"
import { useStoreBasic } from './storeBasic'
import axios from 'axios'
import { ref } from 'vue'

import { useRouter } from 'vue-router'

export const useStoreImage = defineStore('storeImage', {

    state: () => {
        return {
            posts: null,
            comments:null,
            likes:null,
            pets:null,
            follows:null,
            urlDict:new Map(),
            router: useRouter(),
            storeBasic: useStoreBasic()
        }
    },

    actions: {
        async downloadImageURL() {
            this.urlDict = new Map()
            this.posts.forEach((x) => {
            const reference =  storageRef(storage,x.reference)
            getDownloadURL(reference)
                .then(imgURL => {
                  // use Vue.set for reactivity
                  this.urlDict.set(x.reference,imgURL.toString())
                })
            })
        },
        async createUniqueImageRef(user_id, pet_id, file, caption) {
            user_id = user_id.toString()
            pet_id = pet_id.toString()
            const timestamp = Date.now().toString()
            const reference = 'pets/' + user_id + '_' + pet_id + '_' + timestamp
            const ImageRef = storageRef(storage, reference)
            let postform = {
                "timestamp": timestamp,
                "reference": reference,
                "text": caption,
                "pet_id": pet_id
            }
            console.log(postform)
            this.createPost(postform).then(async() => {
                await uploadBytes(ImageRef, file).then((snapshot) => {
                    console.log('Uploaded a blob or file! =>', snapshot);
                })
            })
            
        },
        async deleteImagesbyRef(postData) {
            this.deletePost(postData).then((res) => {
                try {
                    if (res == true) {
                        deleteObject(postData.reference).then((res) => {
                            console.log("post image deleted by reference")
                            this.router.go()
                        }).catch((error) => {
                            console.log(error)
                        });
                    }
                    else {
                        console.log("not authenticated")
                    }

                }
                catch (err) {
                    console.log(err)
                }
            })
            // Delete the file

        },
        async deletePost(data) {
            let postToDelete = { "post_id": data.id }
            await axios.post('post/delete', postToDelete, {
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(res => {
                console.log(res.data)
                this.storeBasic.get_current_user_by_token()
                return res
            }
            )
        },
        async createPost(data) {
            await axios.post('post/', data, {
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(res => {
                console.log(res)
                this.storeBasic.get_current_user_by_token()
            }
            )
        },
        async get_posts(){
            await axios.get('/post/').then((res) => {
                this.posts = res.data.posts
            })
        },
        async get_likes(){
            await axios.get('/post/likes').then((res) => {
                this.likes = res.data.likes
            })
        },
        async get_comments(){
            await axios.get('/post/comments').then((res) => {
                this.comments = res.data.comments
            })
        },
        async get_pets(){
            await axios.get('/post/pets').then((res) => {
                this.pets = res.data.pets
            })
        },
        async get_follows(){
            await axios.get('/post/follows').then((res) => {
                this.follows = res.data.follows
            })
        },
        async init() {
            await this.get_posts()
            await this.get_comments()
            await this.get_likes()
            await this.get_pets()
            await this.get_follows()
            await this.downloadImageURL()
        },
        
    }

}

)