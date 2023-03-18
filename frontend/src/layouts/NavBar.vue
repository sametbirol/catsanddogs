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
                to="/"
                variant="plain"
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

  
<style scoped>
.link > *{text-decoration: none;color:yellowgreen;margin: 10px;text-transform: lowercase;
}
  
  
</style>