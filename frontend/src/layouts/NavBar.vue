<template>
    <v-container class="w-50">
    <v-card
      class="mx-auto"
      max-width="448"
    >
        <v-app-bar
          class="bg-orange-lighten-2"
          density="comfortable"
          elevation="5"
  
        >
          <v-app-bar-title>Purrpawlia</v-app-bar-title> 
            <div class="link" >
              <v-btn
                class="bg-orange-darken-1"
                to="/mainpage"
                variant="plain"
              >
              Posts </v-btn>
              <v-btn
                
                
                class="bg-orange-darken-1"
                variant="plain"
                @click="store.logout()"
              >
              Log Out </v-btn>
              <v-btn
                class="bg-orange-darken-1"
                to="/profile"
                variant="plain"
              >
              Profile</v-btn>
            </div>       
        </v-app-bar>
    </v-card>
  </v-container>
</template>

<script setup>

import { useStoreBasic } from '@/stores/storeBasic.js'
const store = useStoreBasic()

</script>
<style scoped>
.link > *{text-decoration: none;color:yellowgreen;margin: 10px;text-transform: lowercase;
}
  
  
</style>