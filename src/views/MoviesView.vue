

<template>
    <h2>Movies</h2>
    <div class="movies-page">
        <div v-for="movie in movies" :key="movie.id" class="card-container">
            <div class="card">
                <img :src="movie.poster" alt="movie poster" />
                <div class="card-body">
                    <h5 class="card-title">{{ movie.title }}</h5>
                    <p class="card-text">{{ movie.description }}</p>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

let movies = ref([]);

async function fetchMovies() {
const response = await axios.get("/api/v1/movies");
movies.value = response.data.movies;
}
  
onMounted(fetchMovies);
</script>

<style>
.card {
border: 1px solid #ccc;
margin: 1em;
padding: 1em;
display: inline-block;
}
</style>
