<script>
export default {
    data() {
        return {
            toggle: false,
        };
    },
    methods: {
        statusChange(e) {
            this.toggle = !this.toggle;
            let icon = e.target.querySelector(".fa")
            if(!icon){
                icon = e.target;
            }
            console.log(icon);
            icon.classList.toggle("fa-check");
            icon.classList.toggle("fa-close")
        },
    }
}   
</script>

<template>
    <button @click="statusChange" 
        class="status-toggle"
        :style="{
        backgroundColor: toggle ? 'Green' : 'red'
      }">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <span class="button-icon"><i class="fa fa-close"></i></span>
    </button>
    
</template>