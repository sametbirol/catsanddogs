<template>
    <v-container class="">
        <v-card clasS="mx-auto" max-width="1600" rounded="0">
            <v-img height="300px" cover class="align-end"
                src="https://png.pngtree.com/thumb_back/fh260/background/20200714/pngtree-modern-double-color-futuristic-neon-background-image_351866.jpg">
                <v-avatar image="@/assets/cat2-yatay.png" size="150" class="ml-2 ma-15"></v-avatar>

                <v-card-title class="text-white text-h5">Welcome,my liege!</v-card-title>
            </v-img>
            <Tabs/>
        </v-card>

    </v-container>
</template>
<script setup>
import Tabs from '@/components/tabs.vue';

</script>