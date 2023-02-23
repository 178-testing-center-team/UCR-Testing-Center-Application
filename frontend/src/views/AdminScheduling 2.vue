<script>
import Card from "../components/Card.vue"
import NavBar from "../components/NavBar.vue"
import CornerStyle from "../components/CornerStyle.vue"
import Header from "../components/Header.vue";
import Calendar from '../components/Calendar.vue'
import NavBtn from "../components/NavBtn.vue";
import axios from "axios";
export default {
    components: {
        Card,
        NavBar,
        Header,
        CornerStyle,
        Calendar,
        NavBtn
    }
}

</script>



<template>
     <div class="page-content">
        <Header :title="this.$route.params.bldg + ' ' +this.$route.params.room"/>

        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements="[
        { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/admin' },
        { title: 'Rooms', img: 'roomNav-icon.svg', route: '/admin/rooms' },
        { title: 'Inbox', img: 'mailNav-icon.svg', route: '/admin/inbox' },
        { title: 'Settings', img: 'settings-icon.svg', route: '/admin/settings' },
        { title: 'My Account', img: 'profile-icon.svg', route: '/admin/account' }]" />

        <NavBtn />       

        <div class="dp-container">
            <Calendar/>
        </div>

        <CornerStyle/>
    </div> 
</template>
