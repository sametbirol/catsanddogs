<template>
    <v-tabs
      v-model="active_tab"
      bg-color="accent-darken-2"
      fixed-tabs
    >
      <v-tab
        v-for="tab in tabs"
        :key="tab.id"
        :value="tab.id"
      >
      {{ tab.name }}
      </v-tab>
    </v-tabs>
    <v-container>
          <v-card elevation="4" light tag="section">
            <v-card-title>
              <v-layout align-center justify-space-between>
                <h3 class="headline">
                  {{  formTitle }}
                </h3>
                
              </v-layout>
            </v-card-title>
            <v-divider></v-divider>
            <v-card-text>
              <p>Sign in with your username and password:</p>
              <v-form
              id="myInput"
              v-autofocus
              >
                <v-text-field
                              outline
                              label="Username"
                              type="text"
                              v-model="credential.email"
                              v-autofocus></v-text-field>
                <v-text-field
                              outline
                              hide-details
                              label="Password"
                              type="password"
                              v-model="credential.password"></v-text-field>
              </v-form>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions >
              
              <v-spacer></v-spacer>
              <v-btn color="info" id="myBtn" type="submit" @click="onsubmit" v-keyenter>
                {{formTitle}}
              </v-btn>
            </v-card-actions>
          </v-card>

    </v-container>
    <pickyoursideModal
    v-model="modals.pickyourside"
    v-autofocus
    >
    </pickyoursideModal>
</template>

<script setup>
import { ref,computed, reactive} from 'vue'
import pickyoursideModal from '@/modals/pickyourside.vue'
import { vAutofocus } from '@/directives/vAutofocus';
import { vKeyenter } from '@/directives/vKeyenter';
// import { useStoreAuth } from '@/stores/storeAuth'


// store
// const storeAuth = useStoreAuth()
// login or register
const formTitle = computed(() =>{
  return (active_tab.value == 1 ? 'Login' : 'Register')
})

const active_tab= ref(1)
// tabs
const tabs = [
  
  {
    id: 1,
    name: 'Login'
  },
  {
    id: 2,
    name: 'Register'
  },
]
/*
  modals
*/
const modals = reactive({
  pickyourside: true ,
  starwarseffect:true,
})
/*
  credential
*/
const credential = reactive({
  email: '',
  password: '',
})
/*  
  submit
*/
const onsubmit = () => {
  if (!credential.email || !credential.password) {
    alert('Please enter your email and password')
  }
  else {
    if(active_tab.value == 2) {
      console.log('register credential:', credential)
      // storeAuth.createUser(credential)
    }
    else {
      console.log('login credential:', credential)
      // storeAuth.loginUser(credential)
    }
  }
}
</script>