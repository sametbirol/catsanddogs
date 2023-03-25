<template>
    <v-card elevation="4" light tag="section">
        <v-card-title>
            <v-layout align-center justify-space-between>
                <h3 class="headline">
                    Register 
                </h3> <v-spacer></v-spacer>
                <h4 :class="store.msgg == 'User succesfully created' ? 'bg-green' : 'bg-red' ">
                    {{ store.msgg}}
                </h4>

            </v-layout>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text>
            <v-form id="my-form" >
                <v-text-field outline label="Username" type="text" v-model="credential.username" ></v-text-field>
                <v-text-field outline label="Email" type="text" v-model="credential.email" ></v-text-field>
                <v-text-field outline label="FirstName" type="text" v-model="credential.first_name" ></v-text-field>
                <v-text-field outline label="LastName" type="text" v-model="credential.last_name" ></v-text-field>
                <v-text-field outline hide-details label="Password" type="password" v-model="credential.password"></v-text-field>
                <v-text-field outline hide-details label="VerifyPassword" type="password" v-model="credential.verify_password"></v-text-field>
            </v-form>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>

            <v-spacer></v-spacer>
            <v-btn color="info" id="myBtn" type="submit" @click="onsubmit"  >
                Sign Up
            </v-btn>
        </v-card-actions>
    </v-card>
    <pickyoursideModal v-model="modals.pickyourside">
    </pickyoursideModal>
</template>
<script setup>
import { ref, computed, reactive, watch, onBeforeMount,onBeforeUnmount } from 'vue'
import pickyoursideModal from '@/modals/pickyourside.vue'
// import { vAutofocus } from '@/directives/vAutofocus';
// import { vKeyenter } from '@/directives/vKeyenter';
import { useStoreBasic } from '@/stores/storeBasic.js'
import { useRouter } from 'vue-router';
// router

const router = useRouter()
// store
const store = useStoreBasic()

const modals = reactive({
    pickyourside: false,
})
/*
  credential
*/
const credential = reactive({
    "email": "",
    "username": "",
    "first_name": "",
    "last_name": "",
    "password": "",
    "verify_password": "",
})
/*  
  submit
*/
const onsubmit = () => {
    store.createUser(credential)
}

onBeforeMount(() => {
    modals.pickyourside = true
})
</script>