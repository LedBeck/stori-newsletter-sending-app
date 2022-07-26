<script>
import DashboardComponent from './DashboardComponent.vue'
import LoginComponent from './LoginComponent.vue'
const routes = {
  '/login': LoginComponent,
  '/dashboard': DashboardComponent
}

export default {
  data() {
    return {
      currentPath: window.location.hash
    }
  },
  computed: {
    currentView() {
      return routes[this.currentPath.slice(1) || '/'] || NotFound
    }
  },
  mounted() {
    window.addEventListener('hashchange', () => {
		  this.currentPath = window.location.hash
		})
  }
}
</script>

<template>
<nav>
  <a href="#/">Dashboard</a> |
  <!-- <a href="#/about">About</a> -->
  <component :is="currentView" />
</nav>

</template>