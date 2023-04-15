<template>
	<v-card class="mx-auto " color="grey-lighten-3" theme="high-contrast" max width="500">
		<v-row no-gutters class="ma-3 flex-nowrap ">
			<v-col cols="1" class="align-self-end ml-4"><v-avatar color="grey-darken-3"
					image="https://www.shortcurlyhaircuts.net/wp-content/uploads/2018/01/whats-unique-about-girls-with-curly-hair-5.jpg"></v-avatar>
			</v-col>
			<v-col no-gutters cols="7" class="flex-grow-1 flex-shrink-1"><v-list-item-title> 
			{{props.pet["name"] }}</v-list-item-title>
				<v-list-item-subtitle class="font-weight-light"> A Lovely 
				{{props.pet["species"] }}!</v-list-item-subtitle></v-col>
			<v-col no-gutters cols="4" class="flex-grow-1 flex-shrink-0 align-self">
				<v-icon class="me-1" icon="mdi-youtube-subscription"></v-icon>
				<span class="subheading me-2">{{ props.follows.length }}</span>
				<span class="me-1">·</span>
				<v-btn color="orange" size="small" @click="followStatusChange">{{ followed ?
					'Unfollow' : 'Follow' }}</v-btn>
			</v-col>
		</v-row>
		<v-row justify="center">
			<v-img :lazy-src="props.url" :src="props.url" alt="AnimalPhoto" cover class="mt-5 mb-5 " aspect-ratio="1:1" />

		</v-row>

		<v-card-text class="text-h6 py-2 border-b border-t">
			<span class="font-weight-black mr-2">{{ props.poster["username"]}}</span>

			<span>{{ props.post["text"] }}</span>
		</v-card-text>

		<v-card-actions class="ma-2 ">
			<v-row class="d-flex ">
				<v-col cols="3">
					<v-btn size="small" @click="likeStatusChange">
						<v-icon :icon="liked ? 'mdi-heart' : 'mdi-heart-outline'"></v-icon>
					</v-btn>

					<label class="bold"> {{ props.likes.length }}</label>
				</v-col>
				<v-col cols="9">
					<v-row>
						<v-col cols="12">
							<div class="align-right">
								<v-btn prepend-icon="mdi-chat" size="small" variant="text"
									@click="commentsView = !commentsView">
									Comments {{ props.comments.length }}
								</v-btn>
								<div v-if="commentsView" v-for="comment in props.comments" :key="comment.id">
									{{ comment["comment"] }}
								</div>

							</div>
						</v-col>

					</v-row>
				</v-col>
				<v-col>
					<v-text-field append-inner-icon="mdi-send"></v-text-field>
				</v-col>
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
	post: {
		default: null
	},
	comments: {
		default: null
	},
	likes: {
		default: null
	},
	pet: {
		default: null
	},
	follows: {
		default: null
	},
	url: {
		default: null
	},
	poster: {
		default: null
	}
})
const commentsView = ref(false)
const liked = ref(false)
const followed = ref(props.follows.filter(x => x.user_id == storeBasic.user.id).length
)
const likeStatusChange = () => {
	liked.value = !liked.value
	storeImage.get_likes()//replace by post methods, personally prefer passing liked.value to axios.post data for a parameter to either add or delete
}
const followStatusChange = () => {
	if (followed.value == 1) {
		followed.value = 0
	}
	else if (followed.value == 0) {
		followed.value = 1
	}
	storeImage.get_follows()//replace by post methods, personally prefer passing followed.value to axios.post data for a parameter to either add or delete
}
</script>
