<template>
	<v-container>
		<v-row><v-col cols="12"><v-btn class="bg-blue-accent-3" @click="upload_image">Upload</v-btn>
				<uploadphoto v-model="modals.upload"></uploadphoto>
			</v-col>

			<v-col cols="12">
				<div>

					<!-- Username: "{{ storeBasic.user["username"] }}"
					<v-divider thickness="8"></v-divider>
					{{ storeImage.posts[0] }} (first)
					<v-divider thickness="8"></v-divider>
					{{ storeImage.likes[0] }} (first)
					<v-divider thickness="8"></v-divider>
					{{ storeImage.comments[0] }} (first)
					<v-divider thickness="8"></v-divider>
					{{ storeImage.pets[0] }} (first)
					<v-divider thickness="8"></v-divider>
					{{ storeImage.follows[0] }} (first)
					<v-divider thickness="8"></v-divider>
					urlDict.size(also postNumber) : {{ storeImage.urlDict.size }} -->
				</div>
			</v-col>
		</v-row>




		<PostCard v-for="post in storeImage.posts" :key="post.id" :post="post" :comments="commentsFiltered(post.id)"
			:likes="likesFiltered(post.id)" :pet="petFiltered(post.pet_id)" :follows="followsFiltered(post.pet_id)"
			:url="urlFiltered(post.id)" :poster="posterFiltered(post.owner_id)" class="mb-15" />
	</v-container>
</template>

<script setup>
import uploadphoto from '@/modals/uploadphoto.vue';

import PostCard from '@/components/postcarda.vue'
import { useStoreImage } from '@/stores/storeImages';
import { useStoreBasic } from '@/stores/storeBasic';
import { computed, reactive } from 'vue';
const storeBasic = useStoreBasic()
const storeImage = useStoreImage()
/* computed */

const commentsFiltered = computed(() => {
	return (postID) => {
	if (storeImage.comments) {

		return storeImage.comments.filter(x => x.post_id == postID)
	} else {
		return []
	}
	}
})
const likesFiltered = computed(() => {
  return (postID) => {
    if (storeImage.likes) {
      return storeImage.likes.filter(x => x.post_id == postID)
    } else {
      return []
    }
  }
})

const petFiltered = computed(() => {
  return (petID) => {
    if (storeImage.pets) {
      return storeImage.pets.filter(x => x.id == petID)[0]
    } else {
      return null
    }
  }
})

const posterFiltered = computed(() => {
  return (userID) => {
    if (storeImage.users) {
      return storeImage.users.filter(x => x.id == userID)[0]
    } else {
      return null
    }
  }
})

const followsFiltered = computed(() => {
  return (petID) => {
    if (storeImage.follows) {
      return storeImage.follows.filter(x => x.pet_id == petID)
    } else {
      return []
    }
  }
})
const urlFiltered = computed(() => {
  return (postID) => {
    if (storeImage.urlDict && storeImage.posts) {
      return storeImage.urlDict.get(storeImage.posts.filter(x => x.id == postID)[0].reference.toString())
    } else {
      return null
    }
  }
})
const modals = reactive({
	upload: false,

})
const upload_image = () => {
	// console.log(storeImage.urlDict)
	modals.upload = true
	console.log(storeBasic.user)
}
</script>


