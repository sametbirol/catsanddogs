<template>
    <v-card elevation="4" light tag="section">
        <v-card-title>
            <v-layout align-center justify-space-between>
                <h3 class="headline">
                    Login
                </h3>

            </v-layout>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text>
            <p>Sign in with your username and password:{{ store.msg }}</p>
            <v-form id="myInput" v-autofocus>
                <v-text-field outline label="Username" type="text" v-model="credential.username" v-autofocus></v-text-field>
                <v-text-field outline hide-details label="Password" type="password"
                    v-model="credential.password"></v-text-field>
            </v-form>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>

            <v-spacer></v-spacer>
            <v-btn color="info" id="myBtn" type="submit" @click="onsubmit" v-keyenter>
                Login
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script setup>
import { ref, computed, reactive, watch, onBeforeMount } from 'vue'
import { vAutofocus } from '@/directives/vAutofocus';
import { vKeyenter } from '@/directives/vKeyenter';
import { useStoreBasic } from '@/stores/storeBasic.js'
// store
const store = useStoreBasic()
/*
  credential
*/
const credential = reactive({
    username: '',
    password: '',
})
/*  
  submit
*/
const onsubmit = () => {
    if (!credential.username || !credential.password) {
        alert('Please enter your email and password')
    }
    else {
        store.loginUser(credential)
    }
}
/*watch
*/
onBeforeMount(() => {
    store.authenticate_user()
})
</script>
