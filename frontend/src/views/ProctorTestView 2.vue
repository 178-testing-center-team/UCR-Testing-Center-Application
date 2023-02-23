<script>
import NavBar from "../components/NavBar.vue"
import CornerStyle from "../components/CornerStyle.vue"
import Header from "../components/Header.vue";
import NavBtn from "../components/NavBtn.vue";
import StudentCheckInHeader from "../components/StudentCheckInHeader.vue";
import StudentStatusElement from "../components/StudentStatusElement.vue";
import AddRoomButton from "../components/AddRoomButton.vue"
export default {
    components: {
        NavBar, Header, CornerStyle, NavBtn, StudentCheckInHeader, StudentStatusElement, AddRoomButton
    }
}
</script>



<template>
    <div class="page-content">
        <Header title="Room 236 2pm - 3pm"/>
        <NavBtn/>

        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements="[
        { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/proctor' },
        { title: 'Rooms', img: 'roomNav-icon.svg', route: '/proctor/rooms' },
        { title: 'Inbox', img: 'mailNav-icon.svg', route: '/proctor/inbox' },
        { title: 'Settings', img: 'settings-icon.svg', route: '/proctor/settings' },
        { title: 'My Account', img: 'profile-icon.svg', route: '/proctor/account' }]" />
        <div class="student-checkin-container">
            <StudentCheckInHeader/>
            <StudentStatusElement studentName="Gregory Griffith" className="CS131" instructorName="Neftali Watkinson"/>
            <StudentStatusElement studentName="Gregory Griffith" className="CS131" instructorName="Neftali Watkinson"/>
            <StudentStatusElement studentName="Gregory Griffith" className="CS131" instructorName="Neftali Watkinson"/>

        </div>
        <CornerStyle />
    </div>
</template>
