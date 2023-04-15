<template>
    <v-container class="ma-15">

        <div class="bg-grey-lighten-2 ">
            <h3>Following</h3>
        </div>

        <v-card clasS="ma-15 mx-auto" max-width="800" rounded="0">
            <v-img height="100%" cover
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
            <PostCard v-for="post in storeImage.posts.filter(x => x.owner_id == storeBasic.user.id)" :key="post.id"
                :post="post" :comments="commentsFiltered(post.id)" :likes="likesFiltered(post.id)"
                :pet="petFiltered(post.pet_id)" :follows="followsFiltered(post.pet_id)"
                :url="storeImage.urlDict.get(post.reference)" :poster="posterFiltered(post.owner_id)" 
                :item="post.id"
                class="mb-15">
                <template #mySlot v-slot:default="{ post}">


                    <v-col cols="1" justify="end">
                        <v-btn color="rgba(255, 255, 255, 0" @click="modals.delete = true" flat>
                            <svg aria-label="Kapat" class="x1lliihq x1n2onr6" color="rgb(100, 100, 100)"
                                fill="rgb(255, 255, 255)" height="18" role="img" viewBox="0 0 24 24" width="18">
                                <title>Kapat</title>
                                <polyline fill="none" points="20.643 3.357 12 12 3.353 20.647" stroke="currentColor"
                                    stroke-linecap="round" stroke-linejoin="round" stroke-width="3"></polyline>
                                <line fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                    stroke-width="3" x1="20.649" x2="3.354" y1="20.649" y2="3.354"></line>
                            </svg>
                        </v-btn>
                    </v-col>
                    <CloseVerifyModal  v-model="modals.delete" @deletePost="deleteHandle" v-bind:post="post"></CloseVerifyModal>
                </template>
            </PostCard>
        </v-card>

    </v-container>
</template>
<script setup>
import PostCard from '@/components/postcarda.vue'
import { reactive, computed } from 'vue'
import { useStoreBasic } from '@/stores/storeBasic';
import { useStoreImage } from '@/stores/storeImages';
import CloseVerifyModal from '@/modals/CloseVerifyModal.vue';
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
const modals = reactive({
	delete: false,

})
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
const posterFiltered = computed(() => {
    return (userID) => {
        return storeImage.users.filter(x => x.id == userID)[0]
    }
})
const deleteHandle = () => {
    console.log("hello,deletedpost")
}
</script>