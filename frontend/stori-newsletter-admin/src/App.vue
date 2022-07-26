<script>
import DashboardComponent from "./components/DashboardComponent.vue";
import LoginComponent from "./components/LoginComponent.vue";
const routes = {
  "/": LoginComponent,
  "/dashboard": DashboardComponent,
};

export default {
  data() {
    return {
      currentPath: window.location.hash,
      isLogged: true,
    };
  },
  computed: {
    currentView() {
      return routes[this.currentPath.slice(1) || "/"] || NotFound;
    },
  },
  mounted() {
    // Simple routing
    window.addEventListener("hashchange", () => {
      this.currentPath = window.location.hash;
    });
  },
};
</script>

<template>
  <main>
    <!-- <nav>
      <a href="#/dashboard">Dashboard</a>
    </nav> -->

    <component :is="currentView" />
  </main>
</template>
