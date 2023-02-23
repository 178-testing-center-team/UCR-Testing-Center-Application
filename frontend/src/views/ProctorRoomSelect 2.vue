<script>
import Card from "../components/Card.vue"
import NavBar from "../components/NavBar.vue"
import CornerStyle from "../components/CornerStyle.vue"
import Header from "../components/Header.vue";
import NavBtn from "../components/NavBtn.vue";
import RoomCard from '../components/RoomCard.vue';
export default {
    components: {
        Card, NavBar, Header, CornerStyle, NavBtn, RoomCard
    }
}
</script>



<template>
    <div class="page-content">
        <Header title="Testing Rooms"/>
        <NavBtn/>

        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements="[
        { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/proctor' },
        { title: 'Rooms', img: 'roomNav-icon.svg', route: '/proctor/rooms' },
        { title: 'Inbox', img: 'mailNav-icon.svg', route: '/proctor/inbox' },
        { title: 'Settings', img: 'settings-icon.svg', route: '/proctor/settings' },
        { title: 'My Account', img: 'profile-icon.svg', route: '/proctor/account' }]" />
        <div class="room-page-contents">
            <div class = "room-cards">
                <RoomCard cardColor='18ACFF' :roomNum=236 bldg='Winston Chung Hall' :seatNum=45 />
                <RoomCard cardColor='18ACFF' :roomNum=220 bldg='Winston Chung Hall' :seatNum=45 />
            </div>
        </div>
        <CornerStyle />
    </div>
</template>
