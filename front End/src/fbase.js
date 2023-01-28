// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBykpiiKpsH_jP_DGQy2M_zPix83VXmT5U",
  authDomain: "login-3b0a0.firebaseapp.com",
  projectId: "login-3b0a0",
  storageBucket: "login-3b0a0.appspot.com",
  messagingSenderId: "657241205105",
  appId: "1:657241205105:web:1ef19f43330dbaee00aed0",
  measurementId: "G-HJQ4VMLY37"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);