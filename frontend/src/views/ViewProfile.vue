<template>
    <v-container class="ma-15">

        <Sfallow />

        <v-card clasS="ma-15 mx-auto" max-width="800" rounded="0">
            <v-img height="100%" cover class="align-end"
                src="https://png.pngtree.com/thumb_back/fh260/background/20200714/pngtree-modern-double-color-futuristic-neon-background-image_351866.jpg">
                <v-avatar image="@/assets/cat2-yatay.png" size="200" class="ml-2"></v-avatar>

                <v-card-title class="text-white text-h5">Welcome,my liege!</v-card-title>
            </v-img>
            <Tabs/>
        </v-card>

    </v-container>
</template>
<script setup>
import Sfallow from '@/components/sfallow.vue';
import Tabs from '@/components/tabs.vue';

</script>