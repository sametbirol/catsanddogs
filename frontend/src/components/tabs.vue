<template>
	<v-card>
	  <v-tabs
		v-model="tab"
		bg-color="amber"
		fixed-tabs
	  >
		<v-tab value="one">Pets</v-tab>
		<v-tab value="two">Posts</v-tab>
		<v-tab value="three">About</v-tab>
	  </v-tabs>
  
	  <v-card-text>
		<v-window v-model="tab">
		  <v-window-item value="one">
			<v-container>
			<v-row class="flex-row">
				<v-col cols="6"
        		    v-for="soldier in soldiers" :key="soldier">
        		<v-card
        		>
        		<v-avatar image="@/assets/1/hanım.jpeg"></v-avatar> <!-- profile picture of each soldier is hardcoded as hanım, need update-->

        		{{soldier.name}}
        		{{soldier.power}}</v-card>
        		</v-col>
			</v-row>
			</v-container>
		  </v-window-item>
  
		  <v-window-item value="two">
			<v-container class="bg-grey-lighten-2">
			<PostCard v-for="post in storeImage.posts.filter(x => x.owner_id == storeBasic.user.id)" :key="post.id"
                :post="post" :comments="commentsFiltered(post.id)" :likes="likesFiltered(post.id)"
                :pet="petFiltered(post.pet_id)" :follows="followsFiltered(post.pet_id)"
                :url="storeImage.urlDict.get(post.reference)" :poster="posterFiltered(post.owner_id)"
                class="mb-15">
            </PostCard>
		</v-container>
		  </v-window-item>
  
		  <v-window-item value="three">
			<span >
			Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ipsa accusamus aperiam ullam quia ea doloribus velit, molestias veritatis repellendus sed asperiores quaerat esse dolorem tenetur, aspernatur nemo! Sint, rerum veritatis?
			</span>
		  </v-window-item>
		</v-window>
	  </v-card-text>
	</v-card>
  </template>

<script setup>
import PostCard from './postcarda.vue';
import { ref, computed, reactive } from 'vue';
import { useStoreImage } from '@/stores/storeImages';
import { useStoreBasic } from '@/stores/storeBasic';


const tab = ref("two")

const soldiers = reactive({
    soldier1:{
        name:'hanım',
        id:'1',
        power:10000,
    },
    soldier2:{
        name:'pırpır',
        id:'2',
        power:98997,
    }
})

const storeBasic = useStoreBasic()
const storeImage = useStoreImage()

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

</script>