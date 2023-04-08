<template lang="">
    <div class="form-page">
        <h2>Upload Form</h2>
        <MoviesForm />
    </div>
</template>
<script>

import MoviesForm from '../components/MoviesForm.vue';
export default {
    name: "AddMovieFormView",
    components:{
        MoviesForm
    }
}
</script>
<style lang="">
    
</style>