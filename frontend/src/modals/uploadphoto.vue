<template>
    <v-row justify="center">
        <v-dialog v-model="props.modelValue" class="h-screen w-50" persistent>
            <v-form>
                <v-card ref="modalCardRef" class="w-100  h-100 ma-10">


                    <v-card-title class="bg-orange-darken-1 px-8 py-3 white-text">
                        <v-row>
                            <v-col cols="10">Upload Post
                            </v-col>
                            <v-col cols="1">
                                <v-btn class="bg-orange" variant="plain" :hidden="!previewImage"
                                    :disabled="active_tab == 2 ? !petRef || !caption : false" text @click="nextPageUpload"
                                    elevation="2">{{ active_tab == 2 ? 'POST' : 'NEXT' }}
                                </v-btn>
                            </v-col>
                            <v-col cols="1" justify="end">
                                <v-btn color="rgba(255, 255, 255, 0" @click="closeModal" flat>
                                    <svg aria-label="Kapat" class="x1lliihq x1n2onr6" color="rgb(255, 255, 255)"
                                        fill="rgb(255, 255, 255)" height="18" role="img" viewBox="0 0 24 24" width="18">
                                        <title>Kapat</title>
                                        <polyline fill="none" points="20.643 3.357 12 12 3.353 20.647" stroke="currentColor"
                                            stroke-linecap="round" stroke-linejoin="round" stroke-width="3"></polyline>
                                        <line fill="none" stroke="currentColor" stroke-linecap="round"
                                            stroke-linejoin="round" stroke-width="3" x1="20.649" x2="3.354" y1="20.649"
                                            y2="3.354"></line>
                                    </svg>
                                </v-btn>
                            </v-col>
                        </v-row>
                    </v-card-title>
                    <v-row class="ma-10">
                        <v-col cols="12">

                            <v-btn class="bg-blue-accent-4" v-if="!previewImage" @click="onPickFile">Choose from
                                computer</v-btn>
                            <input type="file" accept="image/*" style="display: none" ref="fileInput" @change=uploadImage>

                        </v-col>
                        <v-col :cols="active_tab == 1 ? 12 : 8">


                            <v-img :src="previewImage" class="uploading-image " max-width="500" aspect-ratio="1/1"
                                @click="selected"></v-img>
                        </v-col>
                        <v-divider vertical v-if="active_tab == 2"></v-divider>
                        <v-col v-if="active_tab == 2" cols="4">
                            <v-card>
                                <v-textarea placeholder="Add Caption" v-model="caption">
                                </v-textarea>
                                <v-expansion-panels>
                                    <v-expansion-panel>
                                        <v-expansion-panel-text @click="selected">Pets</v-expansion-panel-text>
                                        <v-radio-group v-model="petRef">
                                            <v-radio v-for="pet in petsFiltered(storeBasic.user.id)" :label="pet.name + ' '+ pet.species"
                                                :value="pet.id"></v-radio>
                                        </v-radio-group>
                                    </v-expansion-panel>
                                </v-expansion-panels>
                            </v-card>
                        </v-col>
                    </v-row>
                </v-card>
            </v-form>
            <!-- <closeVerifyModal v-model="verifyClose" @closeUploadModal="closeModalCall"></closeVerifyModal> -->
        </v-dialog>
    </v-row>
</template>
  
<script setup>
/*
imports
*/
// import { onClickOutside } from '@vueuse/core'
import closeVerifyModal from '@/modals/CloseVerifyModal.vue'
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useStoreBasic } from '@/stores/storeBasic.js'
import { useStoreImage } from '@/stores/storeImages';
// store
const storeBasic = useStoreBasic()
const storeImage = useStoreImage()
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
const caption = ref(null)
const petRef = ref(null)
const imageRef = ref(null)
const active_tab = ref(1)
const previewImage = ref(null)
const fileInput = ref(null)
/*
  handle close clicked
*/
const verifyClose = ref(null)

const emit = defineEmits(['update:modelValue'])
const closeModal = async () => {
    emit('update:modelValue', false)
    free_up_variables()

}
const free_up_variables = () => {
    setTimeout(() => {
        imageRef.value = null
        active_tab.value = 1
        previewImage.value = null
        fileInput.value = null
        caption.value = null
        petRef.value = null
    }, 200);
}
const nextPageUpload = () => {
    active_tab.value += 1
    if (active_tab.value == 3) {
        storeImage.createUniqueImageRef(storeBasic.user.id, petRef.value, imageRef.value, caption.value)
        closeModal()
    }
}
const modalCardRef = ref(null)
const onPickFile = () => {
    fileInput.value.click()
}
const uploadImage = (e) => {
    const image = e.target.files[0];
    const filename = image.name
    if (filename.lastIndexOf('.') <= 0) {
        return alert('Please add a valid file!')
    }
    const reader = new FileReader();
    reader.readAsDataURL(image);
    reader.onload = e => {
        previewImage.value = e.target.result;
        // console.log(previewImage.value);
    };
    imageRef.value = image
    // console.log(image.value)
}
const selected = () => {
    console.log(petRef.value)

}
const petsFiltered = computed(() => {
    return (userID) => {
        return storeImage.pets.filter(x => x.owner_id == userID)
    }
})

</script>
<style>
/* .slide-in-bck-center {
    animation: slide-in-bck-center 1s cubic-bezier(0.550, 0.085, 0.680, 0.530) forwards;
} */

.uploading-image {
    display: flex;
}
</style>