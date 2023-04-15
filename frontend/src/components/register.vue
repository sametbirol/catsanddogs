<template>
    <v-card elevation="4" light tag="section">
        <v-card-title>
            <v-layout align-center justify-space-between>
                <h3 class="headline">
                    Register
                </h3> <v-spacer></v-spacer>
                <h4 :class="store.msgg == 'User succesfully created' ? 'bg-green' : 'bg-red'">
                    {{ store.msgg }}
                </h4>

            </v-layout>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text>
            <v-form id="my-form">
                <v-text-field outline label="Username" type="text" v-model="credential.username"></v-text-field>
                <v-text-field outline label="Email" type="text" v-model="credential.email"></v-text-field>
                <v-text-field outline label="FirstName" type="text" v-model="credential.first_name"></v-text-field>
                <v-text-field outline label="LastName" type="text" v-model="credential.last_name"></v-text-field>
                <v-text-field outline hide-details label="Password" type="password"
                    v-model="credential.password"></v-text-field>
                <v-container class="mr-4">
                    <ul>
                        <li v-if="credential.password.length <= 8" class="text-red">More than 8 characters</li>
                        <li v-if="!/\d/.test(credential.password)" class="text-red">Contains Number </li>
                        <li v-if="!/[A-Z]/.test(credential.password)" class="text-red">Contains Uppercase </li>
                        <li v-if="!format.test(credential.password)" class="text-red">Contains Special Character </li>
                        <!-- 
		            	<li :class="/\d/.test(credential.password) ? 'text-green' : 'text-red'"
                        >Contains Number</li>

		            	<li :class="/[A-Z]/.test(credential.password) ? 'text-green' : 'text-red'"
                        >Contains Uppercase</li>

		            	<li :class="format.test(credential.password) ? 'text-green' : 'text-red'"
                        >Contains Special Character =&rt; [ !@#$%^&*()_+\-=\[\]{};':"\\|,.&lt;&rt;\/?]</li> -->

                    </ul>
                </v-container>
                <v-text-field outline hide-details label="VerifyPassword" type="password"
                    v-model="credential.verify_password"></v-text-field>
                <v-container class="mr-4">
                    <ul>
                        <li v-if="!password_match" class="text-red">Passwords do not match</li>

                    </ul>
                </v-container>
            </v-form>

        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>

            <v-spacer></v-spacer>
            <v-btn color="info" id="myBtn" type="submit" @click="onsubmit" :disabled="!isActive_signup">
                Sign Up
            </v-btn>
        </v-card-actions>
    </v-card>
    <passwordmodal v-if="modals.passworderror" v-model="modals.passworderror"></passwordmodal>

    <pickyoursideModal v-model="modals.pickyourside">
    </pickyoursideModal>
</template>
<script setup>
import { ref, computed, reactive, watch, onBeforeMount, onBeforeUnmount } from 'vue'
import pickyoursideModal from '@/modals/pickyourside.vue'
import passwordmodal from '@/modals/CloseVerifyModal.vue';
import { useStoreBasic } from '@/stores/storeBasic.js'
import { useRouter } from 'vue-router';
// router
const router = useRouter()
// store
const store = useStoreBasic()
// modals
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
/*  
submit
*/
const isActive_signup = computed(() => {
    console.log(password_match.value)
    return credential.email && credential.password && credential.username && credential.first_name && credential.last_name && password_match.value && store.checkPassword(credential.password)
})
const password_match = computed(() => {
    if (credential.password === credential.verify_password) {
        if (credential.password == '') {
            return false
        }
        return true
    }
    return false
})

const onsubmit = () => {
    if (store.checkPassword(credential.password)) {
        store.createUser(credential)
    }
    else {
        modals.passworderror = true
    }
}
/* verify_password */
const verify_password_match = ref(null)
const typing = ref(Date.now())
const format = /[ !@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/

const userTyping = ref(null)
let typingnow = setTimeout(() => {
    userTyping.value = false;
}, 2000);
watch(() => userTyping.value, (newValue) => {
    if (newValue == false) {
        verify_password_match.value = credential.password === credential.verify_password
        // clearTimeout(typingnow)
        console.log("verify_password_match.value: ", verify_password_match.value)
    }
    else if (newValue == true) {
        verify_password_match.value = null
    }
})
watch(() => credential.verify_password, (newValue) => {
    userTyping.value = true;
    typingnow
})
//pick
onBeforeMount(() => {
    modals.pickyourside = true
})
</script>