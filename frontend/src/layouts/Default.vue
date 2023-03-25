<template>
    <v-app>
        <NavBar style="z-index: 2;"></NavBar>
    <v-container class="my-15" style="z-index: 1;">
        <RouterView/>
    </v-container>
    </v-app>

</template>
<script setup>
import NavBar from '@/layouts/NavBar.vue'
</script>