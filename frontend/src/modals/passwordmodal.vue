<template>
	<v-row justify="center">
		<v-dialog
		v-model="props.modelValue"
		width="auto"
		>

		<v-card
		ref="modalCardRef"
		>
		<v-card-title class="text-h5">
			Password Error
		</v-card-title>

		<v-spacer></v-spacer>

		<v-card-text>The password you entered does not meet the requirements</v-card-text>

		<v-card-actions>
		<v-row class="d-flex flex-row-reverse mr-2">
			<v-btn
			color="green"
			variant="outlined"
			@click="closeModal">
				OK
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
	}
})

const emit = defineEmits(['update:modelValue'])

const modalCardRef = ref(null)

const closeModal = () => {
	emit('update:modelValue', false)
}

</script>