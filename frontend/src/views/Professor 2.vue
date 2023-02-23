<script>
import Card from "../components/Card.vue"
import NavBar from "../components/NavBar.vue"
import CornerStyle from "../components/CornerStyle.vue"
import Header from "../components/Header.vue";
import NavBtn from "../components/NavBtn.vue";
export default {
    components: {
        Card, NavBar, Header, CornerStyle, NavBtn
    }
}
</script>



<template>
    <div class="page-content">
        <Header title="Instructor Portal"/>
        <NavBtn/>

        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements="[
        { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/professor' },
        { title: 'Rooms', img: 'roomNav-icon.svg', route: '/professor/rooms' },
        { title: 'Inbox', img: 'mailNav-icon.svg', route: '/professor/inbox' },
        { title: 'Settings', img: 'settings-icon.svg', route: '/professor/settings' },
        { title: 'My Account', img: 'profile-icon.svg', route: '/professor/account' }]" />
        <div class="card-container">
            <Card img-name="room-icon.svg" button-header="View Rooms" route="professor/rooms" />
            <Card img-name="email-icon.svg" button-header="View Inbox" route="professor/inbox" />
        </div>
        <CornerStyle />
    </div>
</template>