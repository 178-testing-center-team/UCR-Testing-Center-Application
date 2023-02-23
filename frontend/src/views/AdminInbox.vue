<script>
import Card from "../components/Card.vue"
import NavBar from "../components/NavBar.vue"
import NavBtn from "../components/NavBtn.vue";
import Header from "../components/Header.vue"
import CornerStyle from "../components/CornerStyle.vue"
import AdminNotif from "../components/AdminNotifText.vue"
import AdminNotifButtons from "../components/AdminNotifButtons.vue"

export default {
    components: {
        Card, NavBar, NavBtn, Header, CornerStyle, AdminNotif, AdminNotifButtons
    }
}
</script>

<template>
    <div class="page-content">
        <Header title="Admin Inbox"/>
        <NavBtn/>
        <NavBar :nav-elements="[
            { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/admin' },
            { title: 'Rooms', img: 'roomNav-icon.svg', route: '/admin/rooms' },
            { title: 'Inbox', img: 'mailNav-icon.svg', route: '/admin/inbox' },
            { title: 'Settings', img: 'settings-icon.svg', route: '/admin/settings' },
            { title: 'My Account', img: 'profile-icon.svg', route: '/admin/account' }]" />
        <div class="admin-notif-container">
            <AdminNotif profName='Allan Knight' className='CS061' roomNum='234' schedDate="2/16/2024" schedTimeFrom="10:00AM" schedTimeTo="4:00PM"/>
            <AdminNotif profName='Allan Knight' className='CS061' roomNum='334' schedDate="3/16/2024" schedTimeFrom="1:00PM" schedTimeTo="4:00PM"/>
            <AdminNotif profName='Allan Knight' className='CS061' roomNum='234' schedDate="2/16/2024" schedTimeFrom="10:00AM" schedTimeTo="4:00PM"/>
            <AdminNotif profName='Allan Knight' className='CS061' roomNum='334' schedDate="3/16/2024" schedTimeFrom="1:00PM" schedTimeTo="4:00PM"/>
            <AdminNotif profName='Allan Knight' className='CS061' roomNum='234' schedDate="2/16/2024" schedTimeFrom="10:00AM" schedTimeTo="4:00PM"/>
            <AdminNotif profName='Allan Knight' className='CS061' roomNum='334' schedDate="3/16/2024" schedTimeFrom="1:00PM" schedTimeTo="4:00PM"/>
            <AdminNotif profName='Allan Knight' className='CS061' roomNum='234' schedDate="2/16/2024" schedTimeFrom="10:00AM" schedTimeTo="4:00PM"/>
            <AdminNotif profName='Allan Knight' className='CS061' roomNum='334' schedDate="3/16/2024" schedTimeFrom="1:00PM" schedTimeTo="4:00PM"/>
        </div>
        <CornerStyle />
    </div>
</template>