<template>
    <Default/>
</template>
<script setup>
import Default from '@/layouts/Default.vue'
import { useStoreBasic } from '@/stores/storeBasic.js'
import { onBeforeMount} from 'vue';
import { useRouter } from 'vue-router';
const router =useRouter()
const store = useStoreBasic()
onBeforeMount(() => {
    store.init()
})
</script>