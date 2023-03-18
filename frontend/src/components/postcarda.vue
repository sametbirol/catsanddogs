<template>
<v-card
	  class="mx-auto "
	  color="grey-lighten-3"
	  theme="high-contrast"
	  max width="500"
	>


	<v-list-item class="w-100">
        <template v-slot:prepend>
          <v-avatar
            color="grey-darken-3"
            image="https://www.shortcurlyhaircuts.net/wp-content/uploads/2018/01/whats-unique-about-girls-with-curly-hair-5.jpg"
          ></v-avatar>
        </template>

        <v-list-item-title>{{ bitanem }}</v-list-item-title>

        <v-list-item-subtitle class="font-weight-light">{{store.side}} Lover</v-list-item-subtitle>

        <template v-slot:append>
          <div class="justify-self-end">
			<span></span>
            <v-icon class="me-1" icon="mdi-youtube-subscription"></v-icon>
            <span class="subheading me-2">256</span>
            <span class="me-1">·</span>
			<v-btn color="orange" size="small">Follow</v-btn>
            
          </div>
        </template>
      </v-list-item>

	  <v-divider class="mx-4 mb-1 mt-1"></v-divider>
	

	  

	<v-row justify="center">
			<v-img
    		  src="https://images.unsplash.com/photo-1615751072497-5f5169febe17?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y3V0ZSUyMGRvZ3xlbnwwfHwwfHw%3D&w=1000&q=80"
    		  min-width="600"
    		  max-width="600"
			  height="665"
			  class="mt-5 mb-5"
    		></v-img>
	</v-row>




	  <template v-slot:prepend>
		<v-icon size="x-large"></v-icon>
	  </template>
  
	  <v-card-text class="text-h6 py-2 border-b border-t">
		<span class="font-weight-black mr-2">{{ bitanem }}</span>

		<span style="font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Numquam rem saepe est non illo quia dignissimos, quod odit reprehenderit explicabo molestias pariatur facere, quisquam, provident mollitia adipisci aperiam dolor totam.</span>
	  </v-card-text>
  
	  <v-card-actions>
		<v-row class="d-flex ">
			<v-btn size="small">
				<v-icon icon="mdi-arrow-up"></v-icon>
			</v-btn>

			<label class="bold"> {{ upvotenumber }} </label>
			 

			<v-btn size="small">
				<v-icon icon="mdi-arrow-down"></v-icon>
			</v-btn>

			<div class="align-right">
			<v-btn prepend-icon="mdi-chat" size="small" variant="text">
				Comments
			</v-btn>
			</div>
		</v-row>
	  </v-card-actions>

</v-card>
</template>

<script setup>
import { ref } from 'vue'
import { useStoreBasic } from '@/stores/storeBasic.js'
// store
const store = useStoreBasic()

const upvotenumber = ref("")
upvotenumber.value = 10

const bitanem = ref("Ecem")
</script>
