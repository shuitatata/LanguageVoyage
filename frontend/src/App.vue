<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav>
      <RouterLink to="/">场景列表</RouterLink>
    </nav>
  </header>

  <main>
    <RouterView />
  </main>
</template>

<style>
header {
  padding: 1rem 2rem;
  background: var(--color-background-soft);
  border-bottom: 1px solid var(--color-border);
}

nav {
  max-width: 1200px;
  margin: 0 auto;
}

nav a {
  color: var(--color-text);
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.2s;
}

nav a:hover {
  background-color: var(--color-background-mute);
}

nav a.router-link-active {
  color: var(--color-primary);
  font-weight: 500;
}

main {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}
</style>
