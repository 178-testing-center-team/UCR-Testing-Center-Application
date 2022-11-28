<script>
import Card from "../components/Card.vue"
import NavBar from "../components/NavBar.vue"
import Header from "../components/Header.vue"
export default {
    components: {
        Card, NavBar, Header
    }
}
</script>

<template>
    <div class="admin-inbox">
        <Header title="Admin Inbox"/>
        <NavBar :nav-elements="[
            { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/admin' },
            { title: 'Rooms', img: 'roomNav-icon.svg', route: 'admin/rooms' },
            { title: 'Inbox', img: 'mailNav-icon.svg', route: 'admin/inbox' },
            { title: 'Settings', img: 'settings-icon.svg', route: 'admin/settings' },
            { title: 'My Account', img: 'profile-icon.svg', route: 'admin/account' },
            { title: 'Logout', img: 'logout-icon.svg', route: '/login' }]" />
    </div>
</template>