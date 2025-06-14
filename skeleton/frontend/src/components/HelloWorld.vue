<template>
  <div class="hello">
    <h2>{{ msg }}</h2>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">Error: {{ error }}</div>
    <div v-else>
      <p>Backend Status: {{ backendStatus }}</p>
      <button @click="fetchData">Refresh</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export default {
  name: 'HelloWorld',
  data() {
    return {
      msg: 'Welcome to Your FastAPI + Vue.js App',
      backendStatus: null,
      loading: false,
      error: null
    }
  },
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      this.loading = true
      this.error = null
      try {
        const response = await axios.get(`${API_URL}/health`)
        this.backendStatus = response.data.status
      } catch (err) {
        this.error = err.message
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.hello {
  padding: 2rem;
}

button {
  background-color: #42b983;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 1rem;
}

button:hover {
  background-color: #369870;
}
</style>
