<template>

	<v-container>
		<v-btn class="bg-blue-accent-3" @click="upload_image">Upload</v-btn>
        <uploadphoto v-model="modals.upload" ></uploadphoto>


		<div>
	{{ storeBasic.user }}
	<v-divider thickness="8"></v-divider>
	{{ storeImage.posts }}
	<v-divider thickness="8"></v-divider>
	{{ storeImage.likes }}
	<v-divider thickness="8"></v-divider>
	{{ storeImage.comments }}
	<v-divider thickness="8"></v-divider>
	{{ storeImage.pets }}
	<v-divider thickness="8"></v-divider>
	{{ storeImage.follows }}
</div>
		<PostCard 
		v-for="post in storeImage.posts"
		:key="post.id"
		:post="post" 
		:comments="commentsFiltered(post.id)"
		:likes="likesFiltered(post.id)"
		:pet="petFiltered(post.pet_id)"
		:follows="followsFiltered(post.pet_id)"
		:url="url(post)"
		class="mb-15"/>
	</v-container>

</template>

<script setup>
import uploadphoto from '@/modals/uploadphoto.vue';

import PostCard from '@/components/postcarda.vue'
import { useStoreImage } from '@/stores/storeImages';
import { useStoreBasic } from '@/stores/storeBasic';
import { computed,reactive} from 'vue';
const storeBasic = useStoreBasic()
const storeImage = useStoreImage()
const commentsFiltered = computed(() => {
	return (postID) => {
		return storeImage.comments.filter(x => x.post_id == postID)
	}
})
const likesFiltered = computed(() => {
	return (postID) => {
		return storeImage.likes.filter(x => x.post_id == postID)
	}
})
const petFiltered = computed(() => {
	return (petID) => {
		return storeImage.pets.filter(x => x.id == petID)[0]
	}
})
const url = computed(() => {
	return async(post) => {
		return await storeImage.downloadImageURL(post)
	}
})
const followsFiltered = computed(() => {
	return (petID) => {
		return storeImage.follows.filter(x => x.pet_id == petID)
	}
})
const modals = reactive({
    upload: false,

})
const upload_image= () => {
    modals.upload = true
}
</script>


