<template>
    <v-container class="ma-15">
    
    
    <v-card clasS="ma-15 ">
        <v-avatar image="@/assets/cat2-yatay.png" size="150"></v-avatar>
        <v-card-title>Welcome,my liege!</v-card-title>
        <v-row class="flex-row"><v-col cols="6"
            v-for="soldier in soldiers">
        <v-card
        >
        <v-avatar image="@/assets/1/hanım.jpeg"></v-avatar> <!-- profile picture of each soldier is hardcoded as hanım, need update-->

        {{soldier.name}}
        {{soldier.power}}</v-card>
        </v-col></v-row>

    </v-card>
    
    </v-container>

</template>
<script setup>
import { reactive} from 'vue'

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