<template>
    <v-container class="ma-15">
    
        <div class="bg-grey-lighten-2 ">
            <h3>Following</h3>
        </div>
    
    <v-card clasS="ma-15 mx-auto"
        max-width="800"
        rounded="0">
        <v-img height="100%"
                cover
                src="https://png.pngtree.com/thumb_back/fh260/background/20200714/pngtree-modern-double-color-futuristic-neon-background-image_351866.jpg">
            <v-avatar image="@/assets/cat2-yatay.png" size="150"></v-avatar>
            
            <v-card-title class="text-white text-h5">Welcome,my liege!</v-card-title>
        </v-img>
        <v-container>
            <v-row class="flex-row">
                <v-btn variant="plain">About </v-btn>
                <v-btn variant="plain">About</v-btn>
                <v-btn variant="plain">About</v-btn>
            </v-row>
        </v-container>
            <v-row class="flex-row">
                <v-col cols="6"
                v-for="soldier in soldiers" :key="soldier">
                <v-card
                >
                <v-avatar image="@/assets/1/hanım.jpeg"></v-avatar> <!-- profile picture of each soldier is hardcoded as hanım, need update-->

                {{soldier.name}}
                {{soldier.power}}</v-card>
            </v-col></v-row>
            <v-btn class="bg-blue-accent-3" @click="upload_image">Upload</v-btn>
        <uploadphoto v-model="modals.upload" ></uploadphoto>

    </v-card>
    
    </v-container>

</template>
<script setup>
import { reactive} from 'vue'
import uploadphoto from '@/modals/uploadphoto.vue';

const modals = reactive({
    upload: false,

})
const upload_image= () => {
    modals.upload = true
}

const soldiers = reactive({
    soldier1:{
        name:'hanım',
        id:'1',
        power:10000,
    },
    soldier2:{
        name:'pırpır',
        id:'2',
        power:98997,
    }
})

</script>