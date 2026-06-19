<script setup>
import { onMounted, ref } from 'vue';

  
    const memes = ref([]);

    async function fetchMemes() {
        try {
            // configure backend base URL via VITE_API_BASE in .env (falls back to localhost:8000)
            const apiBase = import.meta.env.VITE_API_BASE || 'http://127.0.0.1:8000';
            const url = `${apiBase.replace(/\/$/, '')}/api/meme/`;
            const response = await fetch(url, { mode: 'cors' });
            if (!response.ok) {
                const text = await response.text().catch(() => '');
                console.error(`HTTP error ${response.status}`, text);
                return;
            }
            const data = await response.json().catch(() => null);
            memes.value = data?.results ?? data ?? [];
        } catch (err) {
            console.error('Failed to fetch memes:', err);
            memes.value = [];
        }
    }

onMounted(fetchMemes);
</script>

<template>
    <h2>Meme List</h2>

    <div v-for="meme in memes" :key="meme.id" class="meme-item">
        <h3>{{ meme.title || 'No meme available' }}</h3>
        <p>{{ meme.description || 'No description available' }}</p>
    </div>
</template>
