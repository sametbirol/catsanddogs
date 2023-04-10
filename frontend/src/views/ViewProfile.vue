<template>
    <v-container class="ma-15">
    
        <div class="bg-grey-lighten-2 ">
            <h3>Following</h3>
        </div>
    
    <v-card clasS="ma-15 mx-auto"
        max-width="800"
        rounded="0">
        <v-img height="100%"
                cover
                src="https://png.pngtree.com/thumb_back/fh260/background/20200714/pngtree-modern-double-color-futuristic-neon-background-image_351866.jpg">
            <v-avatar image="@/assets/cat2-yatay.png" size="150"></v-avatar>
            
            <v-card-title class="text-white text-h5">Welcome,my liege!</v-card-title>
        </v-img>
        <v-container>
            <v-row class="flex-row">
                <v-btn variant="plain">pets </v-btn>
                <v-btn variant="plain">posts</v-btn>
                <v-btn variant="plain">About</v-btn>
            </v-row>
        </v-container>
            <PostCard 
		v-for="post in storeImage.posts.filter(x => x.owner_id == storeBasic.user.id)"
		:key="post.id"
		:post="post" 
		:comments="commentsFiltered(post.id)"
		:likes="likesFiltered(post.id)"
		:pet="petFiltered(post.pet_id)"
		:follows="followsFiltered(post.pet_id)"
		class="mb-15">
        </PostCard>
    </v-card>
    
    </v-container>

</template>
<script setup>
import PostCard from '@/components/postcarda.vue'
import { reactive,computed} from 'vue'
import { useStoreBasic } from '@/stores/storeBasic';
import { useStoreImage } from '@/stores/storeImages';
const storeBasic = useStoreBasic()
const storeImage = useStoreImage()




// const soldiers = reactive({
//     soldier1:{
//         name:'hanım',
//         id:'1',
//         power:10000,
//     },
//     soldier2:{
//         name:'pırpır',
//         id:'2',
//         power:98997,
//     }
// })
const postsFiltered = computed(() => {
	return (postID, storeBasic) => {
		return storeImage.posts.filter(x => x.owner_id == storeBasic.user.id)
	}
})
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
const followsFiltered = computed(() => {
	return (petID) => {
		return storeImage.follows.filter(x => x.pet_id == petID)
	}
})
</script>