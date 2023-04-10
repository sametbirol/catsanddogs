
import { initializeApp } from 'firebase/app'
import { getStorage } from "firebase/storage";



const firebaseConfig = {
    apiKey: 'AIzaSyAWztZzW5zJMSXgxRY8oXg_DE2TQ_Ky3wg',
    authDomain: 'catsanddogs-1f761.firebaseapp.com',
    projectId: 'catsanddogs-1f761',
    storageBucket: 'catsanddogs-1f761.appspot.com',
    messagingSenderId: '523626365745',
    appId: '1:523626365745:web:dc78ec6b1aff60cfcb6610'
};

const app = initializeApp(firebaseConfig);
// Initialize Cloud Storage and get a reference to the service
const storage = getStorage(app);

export {
    storage
}