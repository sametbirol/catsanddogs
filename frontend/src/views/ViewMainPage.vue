<template>

	<v-container>
		<PostCard 
		v-for="i in 3" 
		class="mb-15"/>
	</v-container>

</template>

<script setup>

import PostCard from '@/components/postcarda.vue'
import { useStoreBasic } from '@/stores/storeBasic.js'
// store
const store = useStoreBasic()

</script>


