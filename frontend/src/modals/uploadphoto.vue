<template>
    <v-row justify="center">
        <v-dialog v-model="props.modelValue" class="w-75  slide-in-bck-center" height="auto" >
            <v-card ref="modalCardRef">


                <v-card-title class="text-h4  ">
                    Upload photo
                </v-card-title>

                <div>
                    <img :src="previewImage" class="uploading-image w-50" />
                    <v-btn class="bg-blue-accent-5" @click="onPickFile">Pick an image</v-btn>
                    <input type="file" accept="image/*" style="display: none"  ref="fileInput" @change=uploadImage>
                </div>


            </v-card>

        </v-dialog>
    </v-row>
</template>
  
<script setup>
/*
imports
*/
// import { onClickOutside } from '@vueuse/core'
import { ref, onMounted, onUnmounted } from 'vue'
import { useStoreBasic } from '@/stores/storeBasic.js'
// store
const store = useStoreBasic()

/*
props
*/
const props = defineProps({
    modelValue: {
        type: Boolean,
        default: false
    },
    // id:{
    //     type: String,
    //     required: true
    // }
})
/*refs*/
const image = ref(null)
const previewImage = ref(null)
const fileInput = ref(null)
/*
  handle close clicked
*/

const emit = defineEmits(['update:modelValue'])

const closeModal = (side) => {
    emit('update:modelValue', false)
}

const modalCardRef = ref(null)
const onPickFile = () => {
    fileInput.value.click()
}
const uploadImage = (e) => {
                const image = e.target.files[0];
                const filename = image.name
                console.log("filename: ",filename)
                if(filename.lastIndexOf('.') <= 0){
                    return alert('Please add a valid file!')
                }
                const reader = new FileReader();
                reader.readAsDataURL(image);
                reader.onload = e =>{
                    previewImage.value = e.target.result;
                    console.log(previewImage.value);
                };
                image.value = image
                console.log(image.value)
            }

</script>
<style>

.slide-in-bck-center {
    animation: slide-in-bck-center 2s cubic-bezier(0.550, 0.085, 0.680, 0.530) forwards;
}

.uploading-image{
     display:flex;
}

</style>