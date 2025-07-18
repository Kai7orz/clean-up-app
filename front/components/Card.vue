<script setup lang="ts">
    const props = defineProps<{
        image_url:string
    }>();

</script>
<template>
    <!-- 画像と説明文字列 -->
    <!-- 画像自体は親からprops として渡す or Pinia -->
    <!-- 画像urlを受け取って表示するだけの責任 -->
    <div class="flex  items-center gap-10 h-96 size-1/2 w-100 
       bg-gray-200/30 backdrop-blur-lg rounded-md border border-gray-200/30 shadow-lg" >
       <form class="m-4">
         <NuxtImg :src=props.image_url width="500px"  />
       </form>
       <div class="m-4">
          画像の説明
            <div class="about">
                <v-btn elevation="2" >test</v-btn>
              </div>
       </div>
    </div>
</template>


