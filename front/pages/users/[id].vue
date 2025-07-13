<script setup lang="ts">
    const { data } = useFetch("/api/users")
</script>

<template>
    <div>
        user information : {{data}}
    </div>
</template>