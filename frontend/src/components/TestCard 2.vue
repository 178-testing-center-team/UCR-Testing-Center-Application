<script>
export default {
    props: {
        buttonHeader: String,
        imgName: String,
        route: String
    }
}   
</script>

<template>
    <div class="test-card">
        <router-link :to="route">
            <button class="test-card-btn">{{ buttonHeader }}</button>
        </router-link>
    </div>
</template>