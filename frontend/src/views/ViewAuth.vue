<template>
  <v-tabs v-model="active_tab" bg-color="accent-darken-2" fixed-tabs>
    <v-tab v-for="tab in tabs" :key="tab.id" :value="tab.id">
      {{ tab.name }}
    </v-tab>
  </v-tabs>
  <v-container>
    <Login v-if="active_tab == 1 ? true : false"></Login>
    <Register v-if="active_tab == 2 ? true : false"></Register>
  </v-container>
</template>

<script setup>
import { ref, onBeforeMount } from 'vue'
import { useStoreBasic } from '@/stores/storeBasic.js'
import Login from '@/components/login.vue';
import Register from '@/components/register.vue';
// store
const store = useStoreBasic()


const active_tab = ref(1)
// tabs
const tabs = [
  {
    id: 1,
    name: 'Login'
  },
  {
    id: 2,
    name: 'Register'
  },
]

onBeforeMount(() => {
  store.get_current_user_by_token()
})
</script>