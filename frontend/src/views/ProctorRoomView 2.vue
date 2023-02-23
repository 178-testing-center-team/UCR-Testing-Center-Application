<script>
import TestCard from "../components/TestCard.vue"
import NavBar from "../components/NavBar.vue"
import CornerStyle from "../components/CornerStyle.vue"
import Header from "../components/Header.vue";
import NavBtn from "../components/NavBtn.vue";
export default {
    components: {
        TestCard, NavBar, Header, CornerStyle, NavBtn
    }
}
</script>



<template>
    <div class="page-content">
        <Header title="Room 236"/>
        <NavBtn/>

        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements="[
        { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/proctor' },
        { title: 'Rooms', img: 'roomNav-icon.svg', route: '/proctor/rooms' },
        { title: 'Inbox', img: 'mailNav-icon.svg', route: '/proctor/inbox' },
        { title: 'Settings', img: 'settings-icon.svg', route: '/proctor/settings' },
        { title: 'My Account', img: 'profile-icon.svg', route: '/proctor/account' }]" />
        <div class="test-card-container">
            <TestCard button-header="7:00am - 9:00am" route="testTimes/testView" />
            <TestCard button-header="1:00pm - 3:00pm" route="testTimes/testView" />
            
        </div>
        <CornerStyle />
    </div>
</template>
