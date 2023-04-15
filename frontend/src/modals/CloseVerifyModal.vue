<template>
	<v-row justify="center">
		<v-dialog v-model="props.modelValue" width="auto">

			<v-card ref="modalCardRef">
				<v-card-title class="text-h5">
					Delete Post
				</v-card-title>

				<v-spacer></v-spacer>

				<v-card-text>Do you want to delete this post?</v-card-text>

				<v-card-actions>
					<v-row class="d-flex flex-row-reverse mr-2">
						<v-btn color="red" variant="tonal" @click="closeThisModal">
							Cancel
						</v-btn>
						<v-btn color="green" variant="tonal" @click="closeModalConfirm">
							Confirm
						</v-btn>
					</v-row>
				</v-card-actions>

			</v-card>

		</v-dialog>
	</v-row>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
	modelValue: {
		type: Boolean,
		default: false
	},
	post: {
		default: null
	}
})

const emit = defineEmits(['update:modelValue', 'deletePost'])

const modalCardRef = ref(null)

const closeThisModal = () => {
	console.log(props.post)
	emit('update:modelValue', false)
}
const closeModalConfirm = () => {
	emit('deletePost')
	closeThisModal()
}

</script>