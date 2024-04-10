import { createRouter, createWebHistory } from "vue-router";
import Home from "@/pages/HomePage.vue";
import User from "@/pages/UserPage.vue";
import Group from "@/pages/GroupPage.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/home", component: Home },
  { path: "/user", component: User },
  { path: "/group", component: Group },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
});

export default router;
