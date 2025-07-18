<script setup lang="ts">
import {ref} from 'vue';
import { onMounted } from 'vue';
import Card from '@/components/Card.vue'

// image_url を配列の状態として保持しておく
// image_url 配列を取得して v-for で展開することでカードリストを描画する

const alert = (msg: string) => {
  window.alert(msg);
};

const { data: response, error } = await useFetch('/api/images')

if (error.value){
  console.error("Fetch error:",error.value)
}

const blobObjectUrls = ref<string[]>([]);

// 画像を取得し配列に保存する処理
onMounted(async () => {
  const url = "http://fast_api:8000/users/1/";
  try {
   const res = await fetch('/api/proxy', { method: 'POST' });

    console.log("Fetch status:", res.status);

    if (res.ok) {
      const blob = await res.blob();
      const objectUrl = URL.createObjectURL(blob);
      blobObjectUrls.value.push(objectUrl);
      blobObjectUrls.value.push(objectUrl);
    } else {
      console.error("Response not OK:", res.status);
    }
  } catch (err) {
    console.error("Fetch failed:", err);
  }
});
</script>

<template>
  <div class="h-screen w-full bg-gradient-to-br from-violet-300 via-pink-200 to-orange-100">
    <!-- <p> useFetch 取得データ : {{response}} </p> -->
    
    <div class="flex justify-center">
      <div v-for="blobObjectUrl in blobObjectUrls" class="m-10">
        <Card :image_url="blobObjectUrl" />
      </div>   
    </div>
  </div>
</template>
