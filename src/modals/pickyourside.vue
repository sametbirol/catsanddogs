<template>
  <v-row justify="center">
    <v-dialog
      v-model="props.modelValue"
      class="w-75  slide-in-bck-center"
      height="auto"
      persistent
    >
      
      <v-card
        ref="modalCardRef"
      >
      <v-row class="w-auto">
      <v-col
      cols="6">
        <v-img
          src="@/assets/cat1.png"
          cover
          class="text-white"
          @click="closeModal"
        ></v-img>
      </v-col>
      <v-col
      cols="6">
        <v-img
          src="@/assets/dog.png"
          cover
          class="text-white"
          @click="closeModal"
        ></v-img>
      </v-col>
    </v-row >
        <v-card-title class="text-h4  ">
          Are you ready to fight for the glory?
        </v-card-title>

        <v-card-text class="h-auto  ">
        <div class="scroll-text">
          On a distant planet called Purrpawlia, cats and dogs had long been at odds with each other. They lived in separate territories and would often engage in fights and skirmishes whenever they crossed paths. The planet was in a constant state of chaos, and neither species seemed willing to make the first move towards peace.<br>

          <br>One day, a mysterious figure appeared on Purrpawlia, claiming to have the power to bring about an end to the long-standing feud between the cats and dogs. This figure, known only as the Mediator, had a unique ability to understand both feline and canine languages and cultures. The Mediator offered to bring the two species together and negotiate a lasting peace.

          <br><br>The cats and dogs were skeptical at first, but the Mediator's reputation preceded them, and eventually, both sides agreed to a summit. The Mediator facilitated discussions between the two species, helping them to understand each other's needs and concerns.

          <br><br>As the talks progressed, it became clear that both cats and dogs had been wronged by the other at different points in their history. They realized that the only way to move forward was to forgive each other and find common ground.

          <br><br>The Mediator's efforts paid off, and the cats and dogs signed a peace treaty, agreeing to coexist peacefully on Purrpawlia. The once-chaotic planet began to thrive, and the two species started to interact more frequently, discovering they had much in common.

          <br><br><b>As the reader of this story, do you think you could help each side maintain their newfound peace and understanding? </b>
        </div>
        </v-card-text>

      
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script setup>
/*
imports
*/
import { onClickOutside } from '@vueuse/core'
import { ref,onMounted,onUnmounted } from 'vue';
// import { useStoreNotes } from '@/stores/storeNotes';
/*
    stores
*/ 
    // const storeNotes = useStoreNotes()
/*
emits
*/
const emit = defineEmits(['update:modelValue'])
/*
props
*/
const props = defineProps({
    modelValue : {
        type: Boolean,
        default: false
    },
    // id:{
    //     type: String,
    //     required: true
    // }
})
/*
  handle close clicked
*/
const closeModal = () => {
    emit('update:modelValue',false)
}
/*
refs
*/
const modalCardRef = ref(null)
/*
on clik outside
*/
onClickOutside(modalCardRef,closeModal)
/*
keyboard control for esc
*/
const handleKeyboard = e => {
        if(e.key  === 'Escape') closeModal()
}
onMounted(() => {
    document.addEventListener('keyup', handleKeyboard)
})
onUnmounted(() => {
    document.removeEventListener('keyup', handleKeyboard)
})

</script>
<style>
.scroll-text{
    font-size: 2vw;
    line-height:1;
    font-weight: 300;
    text-align:justify;
    position: relative;
    animation: scroll 60s    forwards;

}
.slide-in-bck-center {
	animation: slide-in-bck-center 2s cubic-bezier(0.550, 0.085, 0.680, 0.530) forwards;
}

@keyframes slide-in-bck-center {
  0% {
    transform: translateZ(600px);
    opacity: 0;
  }
  100% {
    transform: translateZ(0);
    opacity: 1;
  }
}

</style>