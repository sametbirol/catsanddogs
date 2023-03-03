<template>

	<v-container class="">
		<PostCard 
		v-for="i in 3" 
		class="mb-15"/>
	</v-container>

</template>

<script setup>

import PostCard from '@/components/postcard.vue'
import { useStoreBasic } from '@/stores/storeBasic.js'
// store
const store = useStoreBasic()

</script>


