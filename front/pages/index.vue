<script setup lang="ts">


const alert = (msg: string) => {
  window.alert(msg);
};

const { data: response, error } = await useFetch('/api/images')

if (error.value){
  console.error("Fetch error:",error.value)
}

</script>

<template>
  <div>
    <p> useFetch 取得データ : {{response}} </p>

    <UploadButton
      :config="{
        endpoint: 'imageUploader',
        onClientUploadComplete: (file) => {
          console.log('uploaded', file);
          alert('Upload complete');
        },
        onUploadError: (error) => {
          console.error(error, error.cause);
          alert('Upload failed');
        },
      }"
    />
    <UploadDropzone
      :config="{
        endpoint: 'imageUploader',
        onClientUploadComplete: (file) => {
          console.log('uploaded', file);
          alert('Upload complete');
        },
        onUploadError: (error) => {
          console.error(error, error.cause);
          alert('Upload failed');
        },
      }"
    />

    <div class="grid grid-cols-3 gap-5 text-lg text-blue-400 text-center"> 
      <div>Test String 1 </div>
      <div>Test String 2 </div>
      <div>Test String 3 </div>
    </div> 


  </div>
</template>
