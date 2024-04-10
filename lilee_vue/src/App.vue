<template>
  <v-app>
    <v-main>
      <v-navigation-drawer class="bg-indigo-darken-1" permanent>
        <v-list-item title="Lilee Demo System"></v-list-item>
        <v-divider></v-divider>
        <v-list-item link title="Home" href="/"> </v-list-item>
        <v-list-item link title="UserPage" href="/user"> </v-list-item>
        <v-list-item link title="GroupPage" href="/group"> </v-list-item>
      </v-navigation-drawer>

      <router-view />

      <v-overlay :model-value="isLoading" class="align-center justify-center">
        <v-progress-circular
          color="purple"
          size="40"
          indeterminate
        ></v-progress-circular>
      </v-overlay>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from "vue";
import { instance } from "@/common/api";

let isLoading = ref(false);

instance.interceptors.request.use(
  (config) => {
    isLoading.value = true;
    return config;
  },
  (error) => {
    isLoading.value = false;
    return Promise.reject(error);
  }
);

instance.interceptors.response.use(
  (response) => {
    isLoading.value = false;
    return response;
  },
  (error) => {
    isLoading.value = false;
    return Promise.reject(error);
  }
);
//
</script>
