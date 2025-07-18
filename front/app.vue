<template>
  <v-app>
  <div>
      <NuxtPage />
      <myFooter />
  </div>
  </v-app>
</template>

<script setup lang="ts">
import  myFooter  from '@/components/Footer.vue'
const alert = (msg: string) => {
  window.alert(msg);
};

</script>

