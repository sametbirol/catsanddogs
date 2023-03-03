<template>
    <v-app>
        <NavBar/>
    <v-container class="my-15">
        <RouterView/>
    </v-container>
    </v-app>

</template>
<script setup>
import NavBar from '@/layouts/NavBar.vue'
</script>