<script>
    import Card from "../components/Card.vue"
    import NavBar from "../components/NavBar.vue"
    import NavBtn from "../components/NavBtn.vue";
    import Header from "../components/Header.vue"
    import CornerStyle from "../components/CornerStyle.vue"

    export default {
        components: {
            Card, NavBar, NavBtn, Header, CornerStyle
    }
}
</script>

<template>
    <div class="page-content">
        <Header title="Testing Rooms"/>
        <NavBtn/>
        <NavBar :nav-elements="[
            { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/admin' },
            { title: 'Rooms', img: 'roomNav-icon.svg', route: 'student/rooms' },
            { title: 'Inbox', img: 'mailNav-icon.svg', route: 'student/inbox' },
            { title: 'Settings', img: 'settings-icon.svg', route: 'student/settings' },
            { title: 'My Account', img: 'profile-icon.svg', route: 'student/account' }]" />
        <CornerStyle />
    </div>
</template>