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
                <v-text-field outline label="Username" type="text" v-model="credential.username"></v-text-field>
                <v-text-field outline label="Email" type="text" v-model="credential.email" ></v-text-field>
                <v-text-field outline label="FirstName" type="text" v-model="credential.first_name" ></v-text-field>
                <v-text-field outline label="LastName" type="text" v-model="credential.last_name" ></v-text-field>
                <v-text-field outline hide-details label="Password" type="password" v-model="credential.password"></v-text-field>
                <v-container class="mr-4">
		            <ul>
		            	<li :class="credential.password.length < 8 ? 'text-decoration-none ' : 'text-decoration-line-through text-green'"
                        >8 Characters</li>

		            	<li :class="/\d/.test(credential.password) ? 'text-decoration-line-through text-green' : 'text-decoration-none'"
                        >Contains Number</li>

		            	<li :class="/[A-Z]/.test(credential.password) ? 'text-decoration-line-through text-green' : 'text-decoration-none'"
                        >Contains Uppercase</li>

		            	<li :class="format.test(credential.password) ? 'text-decoration-line-through text-green' : 'text-decoration-none'"
                        >Contains Special Character</li>
                     
                    </ul>
                </v-container>
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
    <passwordmodal
    v-if="modals.passworderror"
    v-model="modals.passworderror"
    ></passwordmodal>
    
    <pickyoursideModal v-model="modals.pickyourside">
    </pickyoursideModal>
</template>
<script setup>
import { ref, computed, reactive, watch, onBeforeMount,onBeforeUnmount } from 'vue'
import pickyoursideModal from '@/modals/pickyourside.vue'
import passwordmodal from '@/modals/passwordmodal.vue';
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
    passworderror: false
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

const format = /[ !@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/

/*  
  submit
*/
const onsubmit = () => {
    if(store.checkPassword(credential.password))
    {
        store.createUser(credential)
    }
    else{
        modals.passworderror = true
    }
}

onBeforeMount(() => {
    modals.pickyourside = true
})


</script>