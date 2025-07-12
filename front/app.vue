<template>
  <div>
    <NuxtPage />
    <Footer />
  </div>
</template>

<script setup lang="ts">

const alert = (msg: string) => {
  window.alert(msg);
};

</script>

