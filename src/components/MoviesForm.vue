<template lang="">
    <div>
        <form @submit.prevent="saveMovie" id="movieForm" action="Post" enctype="multipart/form-data">
            <div class="form-group mb-3">
                <label for="title"></label>
                <input v-model="title" type="text" class="form-control" placeholder="Enter title of movie">
                <label for="description"></label>
                <textarea v-model="description" id="description" cols="30" rows="10"></textarea>
                <label for="title"></label>
                <input id="file" name="poster" type="file" @change="onSelect" class="form-control">
                <button @click="" type="submit" value="submit">Submit</button>
            </div>
        </form>
    </div>
</template>
<script>
import { ref } from "vue";

let csrf_token = ref("");
let error = ref("");

function getCsrfToken() {
    fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            csrf_token.value = data.csrf_token;
        });
}
export default {
data() {
    return {
    title: '',
    description: '',
    poster: null
    };
},
name: "MoviesForm",
methods: {
    onSelect(event) {
    this.poster = event.target.files[0];
    },
    saveMovie() {
        let movieForm = document.getElementById('movieForm');
        let form_data = new FormData(movieForm);
        form_data.append("title", this.title);
        form_data.append("description", this.description);
        form_data.append("poster", this.poster);
        fetch("/api/v1/movies", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token.value
        },
        body: form_data
        })
        .then(response => {
            return response.json();
        })
        .then(data => {
            error.messages = data
        })
        .catch(error => {
            console.log(error);
        });
    }
},
mounted() {
    getCsrfToken();
}
};
</script>
<style lang="">
</style>
