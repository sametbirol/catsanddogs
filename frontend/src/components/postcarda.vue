<template>
<v-card
	  class="mx-auto "
	  color="grey-lighten-3"
	  theme="high-contrast"
	  max width="500"
	>

	<v-list-item class="w-100">
        <template v-slot:prepend>
          <v-avatar
            color="grey-darken-3"
            image="https://www.shortcurlyhaircuts.net/wp-content/uploads/2018/01/whats-unique-about-girls-with-curly-hair-5.jpg"
          ></v-avatar>
        </template>

        <v-list-item-title> {{ props.pet.name }}</v-list-item-title>

        <v-list-item-subtitle class="font-weight-light"> A Lovely {{props.pet.species}}!</v-list-item-subtitle>

        <template v-slot:append>
          <div class="justify-self-end">
			<span></span>
            <v-icon class="me-1" icon="mdi-youtube-subscription"></v-icon>
            <span class="subheading me-2">{{ props.follows.length }}</span>
            <span class="me-1">·</span>
			<v-btn color="orange" size="small" @click="followStatusChange">{{followed ? 'Unfollow':'Follow'}}</v-btn>
            
          </div>
        </template>
      </v-list-item>

	  <v-divider class="mx-4 mb-1 mt-1"></v-divider>
	

	  

	<v-row justify="center">
			<img
			  :src="props.url"
    		  min-width="600"
    		  max-width="600"
			  height="665"
			  class="mt-5 mb-5"
    		/>
	</v-row>




	  <template v-slot:prepend>
		<v-icon size="x-large"></v-icon>
	  </template>
  
	  <v-card-text class="text-h6 py-2 border-b border-t">
		<!-- <span class="font-weight-black mr-2">{{ bitanem }}</span> -->

		<span style="font-family:'Lucida Sans'">{{ props.post.text}}</span>
	  </v-card-text>
  
	  <v-card-actions>
		<v-row class="d-flex ">
			<v-btn size="small" @click="likeStatusChange">
				<v-icon :icon="liked ? 'mdi-heart' : 'mdi-heart-outline'" ></v-icon>
			</v-btn>

			<label class="bold"> {{ props.likes.length }}</label>

			<div class="align-right">
			<v-btn prepend-icon="mdi-chat" size="small" variant="text" @click="commentsView = !commentsView">
				Comments
			</v-btn>
			<div v-if="commentsView" v-for="comment in props.comments" :key="comment.id">
				{{ comment.comment }}
			</div>
			</div>
		</v-row>
	  </v-card-actions>

</v-card>
</template>

<script setup>
import { ref ,computed} from 'vue'
import { useStoreBasic } from '@/stores/storeBasic.js'
import { useStoreImage } from '@/stores/storeImages';
// store
const storeBasic = useStoreBasic()
const storeImage = useStoreImage()

const props = defineProps({
    post : {
        default: null
    },
	comments : {
		default: null
	},
	likes : {
		default : null
	},
	pet: {
		default: null
	},
	follows: {
		default: null
	},
	url: {
		default : null
	}
})
const commentsView = ref(false)
const liked = ref(false)
const followed = ref(false)
const likeStatusChange = () => {
	liked.value = !liked.value
	storeImage.get_likes()//replace by post methods, personally prefer passing liked.value to axios.post data for a parameter to either add or delete
}
const followStatusChange = () => {
	followed.value = !followed.value
	storeImage.get_follows()//replace by post methods, personally prefer passing followed.value to axios.post data for a parameter to either add or delete
}

// const bitanem = ref("Ecem")
</script>
