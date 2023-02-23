<script>
    export default {
        methods: {
            logOutEvent() {
                this.$store.commit('logout');
                this.$router.push('/login');
                console.log(this.$store.state);
            }
        }
    }
</script>

<template>
    <button @click="logOutEvent" class="nav-comp">
        <img src="@/assets/imgs/logout-icon.svg" alt="logout">
        <h3>logout</h3>
    </button>
</template>